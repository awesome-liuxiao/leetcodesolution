from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in res:
                res[sortedWord].append(word)
            else:
                res[sortedWord] = [word]
        # print(list(res.values()))
        return list(res.values())


x = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
x.groupAnagrams(strs)

strs = ["",""]
x.groupAnagrams(strs)

strs = [""]
x.groupAnagrams(strs)