class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmpStr = str(x)
        idx = len(tmpStr) - 1
        isPalind = False
        for i in tmpStr:
            # print(i+':'+tmpStr[idx])
            if i == tmpStr[idx]:
                isPalind = True
                idx -= 1
            else:
                isPalind = False
                break

        return isPalind

x = Solution()
print(x.isPalindrome(121))
print(x.isPalindrome(-121))
print(x.isPalindrome(10))
print(x.isPalindrome(1))

