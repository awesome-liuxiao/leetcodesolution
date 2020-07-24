from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(ind, i, j):
            if self.Found:
                return
            if ind == k:
                self.Found = True
                return
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            tmp = board[i][j]
            # print(ind)
            if tmp != word[ind]:
                return

            board[i][j] = "#"
            for x, y in [[0,-1], [0,1], [1,0], [-1,0]]:
                dfs(ind+1, i+x, j+y)
            board[i][j] = tmp

        self.Found = False
        m, n, k = len(board), len(board[0]), len(word)

        for i in range(m):
            for j in range(n):
                dfs(0, i, j)
        return self.Found

X = Solution()

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"
print(X.exist(board, word))

word = "SEE"
print(X.exist(board, word))

word = "ABCB"
print(X.exist(board, word))
