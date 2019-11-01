class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        needleLen = len(needle)
        haystackLen = len(haystack)
        p = 0 # a pointer to mark position
        res = -1
        checker = False
        while haystackLen-p >= needleLen: # if the pointer reached the position where the remained length is less than the needleLen, end
            if haystack[p] == needle[0]:
                for i in range(needleLen): # if the element in the pointer's position matches the first element in needle, then check the rest
                    if haystack[i+p] == needle[i]:
                        checker = True
                    else:
                        checker = False
                        break # if even one element doesn't match in this round, break.
                    # print(p)
                    # print("haystack["+str(i+p)+"]: "+haystack[i+p]+", needle["+str(i)+"]: "+needle[i])

            if checker == True:
                res = p
                break # if this round all match, then break. no need to keep while-ing
            else:
                p += 1 # if not all match, move pointer to next position
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