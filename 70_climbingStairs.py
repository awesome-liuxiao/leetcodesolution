class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        steps = [1,1]
        for i in range(2,n+1):
            steps.append(steps[i-1]+steps[i-2])
        print(steps)
        return steps[n]
        
x = Solution()

n = 2
x.climbStairs(n)

n = 3
x.climbStairs(n)