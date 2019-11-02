from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsList = []
        singleLen = len(words[0])
        j = 0
        i = 0
        res = []
        for c in s:
            if i == 0:
                wordsList.append(c)
                i += 1
            elif i<singleLen:
                wordsList[j] += c
                i += 1
            else:
                j += 1
                i = 1
                wordsList.append(c)

        i = 0
        words.sort()
        print(wordsList)
        while i +len(words) <= len(wordsList):
            tmpList = []
            j = i
            for k in range(len(words)):
                tmpList.append(wordsList[j])
                j += 1
            print(tmpList)
            tmpList.sort()
            if tmpList == words:
                print("found")
                res.append(i*singleLen)
            i += 1
        print(res)
        return res


x = Solution()

# s = "barfoothefoobarman"
# words = ["foo","bar"]
# x.findSubstring(s, words)

# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
# x.findSubstring(s, words)

s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
x.findSubstring(s, words)
