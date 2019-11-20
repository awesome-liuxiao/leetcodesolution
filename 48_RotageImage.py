from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        # print(matrix)
        length = len(matrix)
        for i in range(int(length/2)):
            for j in range(length):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[length-i-1][j]
                matrix[length-i-1][j] = tmp

        for i in range(length):
            for j in range(i,length):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # print(matrix)

x = Solution()

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
x.rotate(matrix)

matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
x.rotate(matrix)