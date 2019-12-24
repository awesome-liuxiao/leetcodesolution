from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)]for j in range(m)]
        # dp = [[0]*n] * m # this is a wrong declaration for binary list. it causes all elements change once one element changed.
        dp[0][0] = grid[0][0]
        # print(dp)
        for i in range(1,m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1,n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        # print(dp)
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # print(dp)
        # print(dp[m-1][n-1])
        return dp[m-1][n-1]

x = Solution()

grid = [
  [1,3,1,2],
  [1,5,1,3],
  [4,2,1,2]
]
x.minPathSum(grid)