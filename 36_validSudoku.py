from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidNine(board[i]):
                return False
            col = [c[i] for c in board]
            if not self.isValidNine(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[s][t] for s in [i, i+1, i+2] for t in [j, j+1, j+2]]
                if not self.isValidNine(block):
                    return False
        return True

    def isValidNine(self, row):
        map = {}
        for c in row:
            if c != '.':
                if c in map:
                    return False
                else:
                    map[c] = True
        return True

x = Solution()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(x.isValidSudoku(board))

board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(x.isValidSudoku(board))