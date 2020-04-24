class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        square = 0
        n = 0
        if num == 0:
            return 0
        while square < num:
            square = n*n
            n += 1
        print(square)
        if square == num:
            print(True)
            return True
        else:
            print(False)
            return False
'''better solution (referred)
def isPefctSquare(num):
    theSqrt = num ** (1/2) # num^0.5 is the extract of the root num
    tmpNum = int(theSqrt) # if num can be extracted, then it is an integer, otherwise, it is a decimal
    if theSqrt - tmpNum == 0:
        return True
    else:
        return False
'''


X = Solution()

num = 16
X.isPerfectSquare(num)

num = 14
X.isPerfectSquare(num)