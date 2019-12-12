from typing import List
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        i,j=r0,c0
        sign=1
        result=[[r0,c0]]
        stepSize=1
        while len(result)<R*C:
            for _ in range(stepSize):
                j+=sign
                if i>=0 and i<R and j>=0 and j<C:
                    result.append([i,j])
            for _ in range(stepSize):
                i+=sign
                if i>=0 and i<R and j>=0 and j<C:
                    result.append([i,j])
            sign*=-1
            stepSize+=1
        print(result)
        return result


x = Solution()

R = 1
C = 4
r0 = 0
c0 = 0
x.spiralMatrixIII(R,C,r0,c0)

R = 5
C = 6
r0 = 1
c0 = 4
x.spiralMatrixIII(R,C,r0,c0)