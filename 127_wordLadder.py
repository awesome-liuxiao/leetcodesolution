from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList={x:True for x in wordList}
        if endWord not in wordList: return 0
        queue=[[beginWord,1]]
        while len(queue)>0:
            curr,ans=queue[0]
            del queue[0]
            if curr==endWord:
                return ans
            for i in range(len(curr)):
                for j in range(97,97+26):
                    temp=curr[:i]+chr(j)+curr[i+1:]
                    if temp==endWord: return ans+1
                    if temp in wordList:
                        del wordList[temp]
                        queue.append([temp,ans+1])
        return 0

X = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(X.ladderLength(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(X.ladderLength(beginWord, endWord, wordList))

beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]
print(X.ladderLength(beginWord, endWord, wordList))

beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog"]
print(X.ladderLength(beginWord, endWord, wordList))