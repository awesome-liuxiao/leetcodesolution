from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strDigits = ""
        intDigits = 0
        res = []
        for n in digits:
            strDigits += str(n)
        intDigits = int(strDigits)
        # print(strDigits)
        intDigits += 1
        for i in str(intDigits):
            res.append(int(i))
        # print(res)
        return res


x = Solution()

digits = [1,2,3]
x.plusOne(digits)

digits = [4,3,2,1]
x.plusOne(digits)

digits = [1,2,9,9]
x.plusOne(digits)

digits = [9]
x.plusOne(digits)
