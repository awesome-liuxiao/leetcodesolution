class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        longer = ""
        less = ""
        if len(s) > len(t):
            longer = s
            less = t
        else:
            longer = t
            less = s
        longer = sorted(longer)
        less = sorted(less)
        idx = len(longer) - 1
        for i in range(len(less)):
            if less[i] != longer[i]:
                idx = i
                break
        print(longer[idx])
    
X = Solution()

s = "abcd"
t = "abcde"
X.findTheDifference(s, t)

s = ""
t = "a"
X.findTheDifference(s, t)
