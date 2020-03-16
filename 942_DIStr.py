from typing import List
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        res = []
        minNum = 0
        maxNum = len(S)
        for e in S:
            if e == 'I':
                res.append(minNum)
                minNum += 1
            else:
                res.append(maxNum)
                maxNum -= 1
        res.append(minNum)
        print(res)
        # print("min: "+str(minNum)+", max: "+str(maxNum))
        return res


x = Solution()

S = "IDID" #[0,4,1,3,2]
x.diStringMatch(S)

S = "III" #[0,1,2,3]
x.diStringMatch(S)

S = "DDI" #[3,2,0,1]
x.diStringMatch(S)

S = "DDIIDIDIIDDIIDIIDD"
x.diStringMatch(S)