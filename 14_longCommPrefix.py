from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minStrLen = strs[0]
        minStrNum = 0
        i = 0
        for s in strs:
            if len(s) < minStrLen:
                minStrLen = len(s)
                minStrNum = i
            i += 1
        minStr = strs[minStrNum]
        for c in minStr:
            

data1 = ["flower","flow","flight"]
data2 = ["dog","racecar","car"]
x = Solution()
print(x.longestCommonPrefix(data1))
print(x.longestCommonPrefix(data2))