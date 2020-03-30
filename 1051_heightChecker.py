from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        steps = 0
        length = len(heights)
        if length > 1:
            sortedHeights = sorted(heights)
            for i in range(length):
                if sortedHeights[i] != heights[i]:
                    steps += 1
        print(steps)
        return steps

x = Solution()

heights = [5,1,2,3,4] #5
x.heightChecker(heights)

heights = [1,2,3,4,5] #0
x.heightChecker(heights)

heights = [1] #0
x.heightChecker(heights)