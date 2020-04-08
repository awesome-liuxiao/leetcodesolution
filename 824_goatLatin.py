class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ['a','e','i','o','u']
        wordList = S.split()
        cnt = 0
        res = []
        for word in wordList:
            cnt += 1
            if word[0].lower() in vowels:
                word += "ma"
                for i in range(cnt):
                    word += "a"
            else:
                vowel = word[0]
                word = word[1:]+vowel+"ma"
                for i in range(cnt):
                    word += "a"
            res.append(word)
        print(" ".join(res))
        return " ".join(res)

x = Solution()

S = "I speak Goat Latin"
x.toGoatLatin(S)

S = "The quick brown fox jumped over the lazy dog"
x.toGoatLatin(S)