from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = 0
        nums.append(target)
        nums.sort()
        res = nums.index(target)
        # print(res)
        return res
        

x = Solution()

nums = [1,3,5,6]
target = 5
x.searchInsert(nums, target) # 2

nums = [1,3,5,6]
target = 2
x.searchInsert(nums, target) # 1

nums = [1,3,5,6]
target = 7
x.searchInsert(nums, target) # 4

nums = [1,3,5,6]
target = 0
x.searchInsert(nums, target) # 0