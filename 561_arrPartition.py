from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        pairs = []
        nums.sort()
        i = 0
        while i < len(nums)-1:
            res += min(nums[i], nums[i+1])
            pairs.append([nums[i],nums[i+1]])
            i += 2
        # print(pairs)
        print(res)
        return res

X = Solution()

nums = [1,4,3,2]
X.arrayPairSum(nums)