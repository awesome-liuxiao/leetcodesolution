class Solution:
    def reverse(self, x: int) -> int:
        tmpStr = str(x)
        if len(tmpStr) == 1:
            return tmpStr
        res = ""
        while True:
            if tmpStr[len(tmpStr)-1] == '0':
                tmpStr = tmpStr[0:len(tmpStr)-1]
            else:
                break

        if tmpStr[0].isdigit():
            res = ""
        else:
            res = tmpStr[0]
            tmpStr = tmpStr[1:]

        strLen = len(tmpStr)
        for i in range(strLen):
            res += tmpStr[strLen-1-i]

        intRes = int(res)
        if intRes >= pow(-2,31) and intRes <= pow(2, 31) - 1:
            return intRes
        else:
            return 0

# x = Solution()
# print(x.reverse('1534236469'))
# print(x.reverse('-1'))
# print(x.reverse('120'))