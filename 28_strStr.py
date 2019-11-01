class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        needleLen = len(needle)
        haystackLen = len(haystack)
        p = 0
        res = -1
        checker = False
        while haystackLen-p >= needleLen:
            if haystack[p] == needle[0]:
                for i in range(needleLen):
                    if haystack[i+p] == needle[i]:
                        checker = True
                    else:
                        checker = False
                        break
                    # print(p)
                    # print("haystack["+str(i+p)+"]: "+haystack[i+p]+", needle["+str(i)+"]: "+needle[i])

            if checker == True:
                res = p
                break
            else:
                p += 1
        return res

x = Solution()
haystack1 = "hello"
needle1 = "ll"
haystack2 = "aaaaa"
needle2 = "bba"
haystack3 = "a"
needle3 = "a"
print(x.strStr(haystack1, needle1))
print(x.strStr(haystack2, needle2))
print(x.strStr(haystack3, needle3))