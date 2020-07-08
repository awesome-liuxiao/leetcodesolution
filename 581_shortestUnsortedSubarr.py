from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        startIdx = -1
        endIdx = len(nums)+1
        sortedNums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] <= sortedNums[i]:
                endIdx = i
            else:
                if startIdx == -1:
                    startIdx = i
        print(f"startIdx: {startIdx}, endIdx: {endIdx}")
        
X = Solution()

nums = [2, 6, 4, 8, 10, 9, 15]
X.findUnsortedSubarray(nums)

nums = [3,2,1,1,1,1]
X.findUnsortedSubarray(nums)
