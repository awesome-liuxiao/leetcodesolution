from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for li in A:
            tmp = []
            for n in li:
                tmp.insert(0,n)
            res.append(tmp)
        for li in res:
            for i in range(len(li)):
                if li[i] == 0:
                    li[i] = 1
                else:
                    li[i] = 0
        # print(res)
        return res

x = Solution()

A = [[1,1,0],[1,0,1],[0,0,0]]
x.flipAndInvertImage(A)

A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
x.flipAndInvertImage(A)

A = [[1]]
x.flipAndInvertImage(A)