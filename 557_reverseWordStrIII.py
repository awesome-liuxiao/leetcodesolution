class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        sList = s.split()
        for e in sList:
            res += e[::-1] + " "

        print(res[:len(res)-1])
        return res[:len(res)-1]

x = Solution()

s = "Let's take LeetCode contest"
x.reverseWords(s)

s = "a"
x.reverseWords(s)