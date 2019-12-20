from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ways = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            ways[0][0] = 1 
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == j == 0:
                        continue
                    else:
                        ways[i][j] = ways[i-1][j] + ways[i][j-1]
        # print(ways)
        return ways[m-1][n-1]

x = Solution()

obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
x.uniquePathsWithObstacles(obstacleGrid)