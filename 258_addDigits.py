class Solution:
    def addDigits(self, num: int) -> int:
        numStr = str(num)
        tmpSum = 0
        for n in numStr:
            tmpSum += int(n)
        if len(str(tmpSum)) == 1:
            print(tmpSum)
            return tmpSum
        else:
            return self.addDigits(tmpSum)

x = Solution()

num = 38
x.addDigits(num)

num = 258
x.addDigits(num)

num = 99999
x.addDigits(num)