class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for c in s:
            res = ord(c)-64 + res*26
        return res
        print(res)

X = Solution()

s = "A"
X.titleToNumber(s)

s = "AB"
X.titleToNumber(s)

s = "ZY"
X.titleToNumber(s)