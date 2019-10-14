class Solution:
    def maxArea(self, height: List[int]) -> int:
        numOfLines = len(height)
        maxWater = 0
        idx = 1
        for i in numOfLines-1:
            idx = i + 1
            for idx in numOfLines:
                if height[i] >= height[idx]:
                    water = height[idx] * abs(i-idx)
                else:
                    water = height[i] * abs(i-idx)
                if water > maxWater:
                    maxWater = water
        return maxWater

x = Solution()
data1 = [1,8,6,2,5,4,8,3,7]
print(maxArea(data1))