class Solution:
    def reachNumber(self, target: int) -> int:
        sumOfPos = 0
        step = 0
        target = abs(target)
        while sumOfPos < target or (sumOfPos - target) % 2 != 0:
            step += 1
            sumOfPos += step
        print(step)
        return step

'''
If we consider the sequence as 1+2+3+...+n, which means the step only goes left (since the +/- sign doesn't bother the result), then by increasing n, if the sum is bigger than target, and the difference of sum and target is even, then by modify one or more + sign(s) in the sum equation we can reach the target number (this has been proved by manually); if the sum is eaqual to target, then which means we reached the target without changing any sign (the difference is zero so the while loop won't contitue)
'''

X = Solution()

target = 3
X.reachNumber(target)

target = 2
X.reachNumber(target)

target = 1
X.reachNumber(target)

target = pow(10,9)
X.reachNumber(target)

target = pow(-10,9)
X.reachNumber(target)