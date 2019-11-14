from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        moresCode =  [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = set()
        for word in words:
            morse = ""
            for c in word:
                loc = ord(c) - 97
                morse += moresCode[loc]
            trans.add(morse)
        # print(len(trans))
        return len(trans)

x = Solution()

words = ["gin", "zen", "gig", "msg"]
x.uniqueMorseRepresentations(words)