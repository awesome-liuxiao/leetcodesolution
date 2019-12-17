class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        ways = [0]*n
        # print(ways)
        ways[0] = 1
        # print(ways)
        for i in range(m):
            for j in range(1,n):
                ways[j] += ways[j-1]
        # print(ways)
        return ways[n-1]

x = Solution()

m = 3
n = 2
x.uniquePaths(m,n)

m = 7
n = 3
x.uniquePaths(m,n)