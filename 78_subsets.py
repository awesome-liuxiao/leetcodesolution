from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(index, subset): #backtracking
            res.append(subset)
            for i in range(index, len(nums)):
                helper(i+1, subset+[nums[i]])
        helper(0, [])
        print(res)
        return res


X = Solution()

nums = [1,2,3]
X.subsets(nums)