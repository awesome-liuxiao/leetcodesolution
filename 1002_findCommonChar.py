from typing import List
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        isCommon = False
        tmpList = []
        for s in A:
            tmpList.append(list(s))
        for c in tmpList[0]:
            for li in tmpList[1:]:
                if c in li:
                    del li[li.index(c)]
                    isCommon = True
                else:
                    isCommon = False
                    break
            if isCommon:
                res.append(c)
        print(res)
        return res

X = Solution()

A = ["bella","label","roller"]
X.commonChars(A)

A = ["cool","lock","cook"]
X.commonChars(A)

A = ["hh","h"]
X.commonChars(A)