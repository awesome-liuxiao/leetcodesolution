from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]
        minStrLen = len(strs[0])
        minStrNum = 0
        longest = ""
        i = 0
        for s in strs:
            if len(s) < minStrLen:
                minStrLen = len(s)
                minStrNum = i
            i += 1
        minStr = strs[minStrNum]
        del strs[minStrNum]
        i = 0
        for c in minStr:
            tmpEqual = False
            for l in strs:
                # print(c+": "+l[i])
                if c == l[i]:
                    # print(l[i], end="")
                    tmpEqual = True
                else:
                    tmpEqual = False
                    break
            # print()
            i += 1
            if tmpEqual == True:
                longest += c
            else:
                break

        return longest

data1 = ["flower","flow","flight"]
data2 = ["dog","racecar","car"]
data3 = ["c","acc","ccc"]
x = Solution()
print(x.longestCommonPrefix(data1))
print(x.longestCommonPrefix(data2))
print(x.longestCommonPrefix(data3))