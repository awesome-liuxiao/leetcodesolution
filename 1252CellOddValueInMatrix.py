from typing import List
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = []
        col = []
        res = 0
        for j in range(m):
            col.append(0)
        for i in range(n):
            matrix.append(col[:])
        for r, c in indices:
            for i in range(len(matrix[r])):
                # print(r)
                # print()
                matrix[r][i] += 1
                # print(matrix)
            for j in range(len(matrix)):
                matrix[j][c] += 1
        # print(matrix)

        for row in matrix:
            for n in row:
                if n % 2 == 1:
                    res += 1
        # print(res)
        return res

x = Solution()

n = 2
m = 3
indices = [[0,1],[1,1]]
x.oddCells(n,m,indices)


n = 2
m = 2
indices = [[1,1],[0,0]]
x.oddCells(n,m,indices)

m = 1
n = 1
indices = [[0,0]]
x.oddCells(n,m,indices)