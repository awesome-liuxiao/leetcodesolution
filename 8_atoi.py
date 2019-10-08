class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        while s[0] == ' ':
            if len(s) == 1:
                return 0
            else:
                s = s[1:]
        res = ""
        symbol = ""
        if s[0] == '+' or s[0] == '-':
            symbol = s[0]
            if len(s) > 1:
                s = s[1:]
            else:
                return 0
        if s[0].isdigit() == False:
            return 0
        i = 0
        for c in s:
            if c.isdigit():
                res += c
            elif c == '.':
                if int(s[i+1]) >= 5:
                    res = int(res)+1
                    break
                else:
                    res = int(res)
                    break
            else:
                break
            i += 1
        #res = symbol+res
        res = int(symbol + str(res))
        if res < pow(-2, 31):
            return pow(-2, 31)
        elif res > pow(2, 31) - 1:
            return pow(2, 31) - 1
        else:
            return int(res)

x = Solution()
print(x.myAtoi("42"))
print(x.myAtoi("   -42"))
print(x.myAtoi("3.54159"))
print(x.myAtoi("4193 with words"))
print(x.myAtoi("words and 987"))
print(x.myAtoi("-91283472332"))
print(x.myAtoi("   +22"))
print(x.myAtoi("+22"))
print(x.myAtoi("   +"))
print(x.myAtoi("   "))
print(x.myAtoi("  -0012a42"))
print(x.myAtoi("   +0 123"))
print(x.myAtoi(""))