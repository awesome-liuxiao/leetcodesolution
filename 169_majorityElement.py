from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        maxTimes = 0
        major = 0
        while i < len(nums):
            times = nums.count(nums[i])
            if times > maxTimes:
                maxTimes = times
                major = nums[i]
            i += nums.count(nums[i])
        # print(f"major: {major}, maxTimes: {maxTimes}")
        return major
        
X = Solution()

nums = [3,2,3]
X.majorityElement(nums)

nums = [2,2,1,1,1,2,2]
X.majorityElement(nums)

nums = [1,2]
X.majorityElement(nums)
