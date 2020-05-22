from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if nums.count(n) == 1:
                res = n
                break
        # print(res)
        return res
    
X = Solution()

nums = [2,2,1]
X.singleNumber(nums)

nums = [4,1,2,1,2]
X.singleNumber(nums)