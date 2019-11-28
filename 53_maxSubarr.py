from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        res = float('-inf')
        out = res
        for num in nums:
            out = max(out+num, num)
            res = max(out, res)
        # print(res)
        return res


x = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
x.maxSubArray(nums)

nums = []
x.maxSubArray(nums)

nums = [1]
x.maxSubArray(nums)

nums = [1,2]
x.maxSubArray(nums)