class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        isWord = False
        sList = []
        if not s:
            # print(res)
            return res
        sList = s.split()
        # print(sList)
        if not sList:
            # print(res)
            return res
        lastWord = sList[len(sList)-1]
        for c in lastWord:
            if c.isalpha():
                isWord = True
            else:
                isWord = False
        if isWord:
            res = len(lastWord)

        # print(res)
        return res
        

x = Solution()

s = "Hello World"
x.lengthOfLastWord(s)

s = "Hello"
x.lengthOfLastWord(s)

s = "Hello "
x.lengthOfLastWord(s) # 5

s = ""
x.lengthOfLastWord(s)

s = " "
x.lengthOfLastWord(s)

s = "Hello      "
x.lengthOfLastWord(s) # 5

s = "a"
x.lengthOfLastWord(s)