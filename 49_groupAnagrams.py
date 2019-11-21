from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sizeDict = {}
        res = []
        for word in strs:
            tmpSize = self.getSize(word)
            sizeDict[word] = tmpSize
        tmpList = []
        for word in strs:
            i = 0
            for wordd in sizeDict:
                if sizeDict[word] == sizeDict[wordd]:
                    tmpList.append(word)
            print(tmpList)
            if tmpList not in res:
                res.append(tmpList)
            tmpList = []
        print(res)
        return res

    def getSize(self, word):
        size = 0
        for c in word:
            size += ord(c)
        return size

x = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# x.groupAnagrams(strs)

strs = ["",""]
x.groupAnagrams(strs)

strs = [""]
# x.groupAnagrams(strs)