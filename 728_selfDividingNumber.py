from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for n in range(left, right+1):
            nStr = str(n)
            if '0' in nStr:
                continue
            isDividable = False
            for c in nStr:
                if n % int(c) == 0:
                    isDividable = True
                else:
                    isDividable = False
                    break
            if isDividable:
                res.append(n)
        return res

X = Solution()

left = 1
right = 22
print(X.selfDividingNumbers(left, right))
