from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return
        revSortedNums = sorted(nums)[::-1]
        return max(revSortedNums[0]*revSortedNums[1]*revSortedNums[2], revSortedNums[0]*revSortedNums[-1]*revSortedNums[-2])

X = Solution()

nums = [1,2,3]
print(X.maximumProduct(nums))

nums = [1,2,3,4]
print(X.maximumProduct(nums))

nums = [-4,-3,-2,-1,60]
print(X.maximumProduct(nums))
