from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # print("sorted reversed stones: ",end="")
        # print(stones)
        while len(stones) > 1:
            stones.sort()
            stones.reverse()
            if stones[0] == stones[1]:
                del stones[0]
                if len(stones) > 1:
                    del stones[0]
                else:
                    stones = []
            else:
                stones[0] -= stones[1]
                del stones[1]
            # print(stones)
        if stones:
            return stones[0]
        else:
            return 0
        
X = Solution()

stones = [2,7,4,1,8,1]#1
X.lastStoneWeight(stones)

stones = [2,7,4,1,8,1,2,3,4,1,1,5,2,7,12,4]#0
# X.lastStoneWeight(stones)

stones = [7,6,7,6,9]#3
# X.lastStoneWeight(stones)