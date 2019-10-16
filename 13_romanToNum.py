class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
        i = 0
        l = len(s) - 1
        res = romanDict[s[l]]
        #print("res at init: "+str(res))
        for i in range(l):
            if romanDict[s[i]] < romanDict[s[i+1]]:
                res -= romanDict[s[i]]
            else:
                res += romanDict[s[i]]
        return res

x = Solution()
print(x.romanToInt("III"))
print(x.romanToInt("IV"))
print(x.romanToInt("IX"))
print(x.romanToInt("LVIII"))
print(x.romanToInt("MCMXCIV"))