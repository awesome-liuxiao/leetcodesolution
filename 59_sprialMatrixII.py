from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return
        lenOfMatrix = n*n
        row = n
        col = n
        top = 0
        bottom = col
        left = 0
        right = row
        candidates = []
        cur = 1
        for i in range(1,lenOfMatrix+1):
            candidates.append(0)
        res = [candidates[x:x+n] for x in range(0, lenOfMatrix, n)]
        
        while cur <= lenOfMatrix:
            if cur <= lenOfMatrix:
                for i in range(left, right):
                    res[top][i] = cur
                    cur += 1
                top += 1
            # print(res)
            if cur <= lenOfMatrix:
                for i in range(top, bottom):
                    res[i][right-1] = cur
                    cur += 1
                right -= 1
            # print(res)
            if cur <= lenOfMatrix:
                i = right-1
                while i > left:
                    res[bottom-1][i] = cur
                    i -= 1
                    cur += 1
                bottom -= 1
            # print(res)
            if cur <= lenOfMatrix:
                i = bottom
                while i >= top:
                    res[i][left] = cur
                    i -= 1
                    cur += 1
                left += 1
            # print(res)
        # print(res)
        # print(cur)
        return res

x = Solution()

n = 3
x.generateMatrix(n)

n = 4
x.generateMatrix(n)

n = 1
x.generateMatrix(n)

n = 0
x.generateMatrix(n)