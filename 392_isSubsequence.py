class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_flag = 0
        cnt = 0
        for i in range(len(s)):
            for j in range(t_flag, len(t)):
                if s[i] == t[j]:
                    cnt += 1
                    t_flag = j+1
                    break
        if cnt == len(s):
            return True
        else:
            return False
        
X = Solution()

s = "abc"
t = "ahbgdc"
print(X.isSubsequence(s, t))

s = "axc"
t = "ahbgdc"
print(X.isSubsequence(s, t))

s = "aaaaaa"
t = "bbaaaa"
print(X.isSubsequence(s, t))

# import random

# letters = "abcdefghijklmnopqrstuvwxyz"
# s = ""
# t = ""
# for i in range(100):
#     s += random.choice(letters)
# for i in range(pow(10,4)):
#     t += random.choice(letters)
# print(t)
# print(X.isSubsequence(s, t))
