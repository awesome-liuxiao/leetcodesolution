class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for c in s:
            # print(ord(c))
            if ord(c) >= 65 and ord(c) < 97: # where 65 is the decimal ASCII number of 'A', and 97 is the decimal ASCII number of 'a'
                res += chr(ord(c)+32)
            else:
                res += c
        # print(res)
        return res

x = Solution()

s = "Hello"
x.toLowerCase(s)

s = "here"
x.toLowerCase(s)

s = "LOVELY"
x.toLowerCase(s)

s = "al&phaBET"
x.toLowerCase(s)

s = "A"
x.toLowerCase(s)