import collections
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        cnt = collections.Counter(S)
        for c in J:
            res += cnt[c]

        # print(res)
        return res
        
x = Solution()

J = "aA"
S = "aAAbbbb"
x.numJewelsInStones(J,S)

J = "z"
S = "ZZ"
x.numJewelsInStones(J,S)