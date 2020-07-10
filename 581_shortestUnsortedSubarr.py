from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        endIdxList = []
        sortedNums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != sortedNums[i]:
                endIdxList.append(i)
        # print(f"endIdx: {endIdxList}")
        # print(endIdxList[-1] - endIdxList[0] + 1)
        if not endIdxList:
            return 0
        return endIdxList[-1] - endIdxList[0] + 1
        
X = Solution()

nums = [2, 6, 4, 8, 10, 9, 15]
X.findUnsortedSubarray(nums)

nums = [3,2,1,1,1,1]
X.findUnsortedSubarray(nums)
