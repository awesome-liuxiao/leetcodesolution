from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, num in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + num)
        return True

x = Solution()

nums = [2,3,1,1,4]
print(x.canJump(nums))

nums = [3,2,1,0,4]
# x.canJump(nums)