class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return True
        if len(word) == 1:
            return True
        if word[0].isupper():
            if word[1].isupper():
                for c in word[2:]:
                    if c.isupper():
                        continue
                    else:
                        return False
            else:
                for c in word[2:]:
                    if c.islower():
                        continue
                    else:
                        return False
        else:
            for c in word[1:]:
                if c.islower():
                    continue
                else:
                    return False
        return True
        
X = Solution()

word = "USA"
print(X.detectCapitalUse(word))

word = "FlaG"
print(X.detectCapitalUse(word))

word = "leetcode"
print(X.detectCapitalUse(word))

word = "GG"
print(X.detectCapitalUse(word))
