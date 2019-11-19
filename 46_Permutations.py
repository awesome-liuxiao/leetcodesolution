from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        out = []
        self.dfs(nums,out,res)

        print(res)
        return res
       
    def dfs(self, nums, out, res):
        if not nums:
            if out not in res: # for solve prob #47
                res.append(out)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:],out+[nums[i]],res)

x = Solution()

nums = [1,2,3]
x.permute(nums)

nums = []
x.permute(nums)

nums = [1,2,1]
x.permute(nums)