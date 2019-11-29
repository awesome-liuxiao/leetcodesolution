from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return
        if len(matrix) == 1:
            return matrix[0]
        res = []
        row = len(matrix[0])
        col = len(matrix)
        top = 0
        bottom = col
        left = 0
        right = row
        while len(res) < row*col:
            if len(res) < row*col:
                for i in range(left, right):
                    res.append(matrix[top][i])
                top += 1
            if len(res) < row*col:
                for i in range(top, bottom):
                    res.append(matrix[i][right-1])
                right -= 1
            if len(res) < row*col:
                i = right-1
                while i >left:
                    res.append(matrix[bottom-1][i])
                    i -= 1
                bottom -= 1
            if len(res) < row*col:
                i = bottom
                while i >= top:
                    # print(matrix[i][left])
                    res.append(matrix[i][left])
                    i -= 1
                left += 1
        # print(res)
        return res

x = Solution()

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
x.spiralOrder(matrix)

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
x.spiralOrder(matrix)

matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]
]
x.spiralOrder(matrix)

matrix = [[]]
x.spiralOrder(matrix)

matrix = [[1,2,3,4]]
x.spiralOrder(matrix)