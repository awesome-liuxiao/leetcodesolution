class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
                steps += 1 
            else:
                num -= 1
                steps += 1
        print(steps)
        return steps

x = Solution()

num = 14 #6
x.numberOfSteps(num)

num = 8
x.numberOfSteps(num)

num = 123
x.numberOfSteps(num)

num = 35
x.numberOfSteps(num)

num = 69
x.numberOfSteps(num)
