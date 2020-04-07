from typing import List
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = []
        sLen = len(S)
        for i in range(sLen):
            if S[i] == C:
                res.append(0)
            else:
                leftDist = 0
                rightDist = 0
                tmpDist = 0
                for m in range(0,i):
                    tmpDist += 1
                    if S[i-m-1] == C:
                        # print("found in left")
                        leftDist = tmpDist
                        # print(leftDist)
                        tmpDist = 0
                        break
                tmpDist = 0
                for n in range(i+1,sLen):
                    tmpDist += 1
                    if S[n] == C:
                        # print("found in right")
                        rightDist = tmpDist
                        # print(rightDist)
                        # print("i:"+str(i)+"n:"+str(n))
                        tmpDist = 0
                        break
                if leftDist == 0:
                    res.append(rightDist)
                else:
                    if rightDist == 0:
                        res.append(leftDist)
                    else:
                        if leftDist < rightDist:
                            res.append(leftDist)
                        else:
                            res.append(rightDist)

        print(res)
        return res

x = Solution()

S = "loveleetcode"
C = 'e'
x.shortestToChar(S,C)