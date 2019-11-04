from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        while target in nums:
            res.append(nums.index(target))
            nums[nums.index(target)] = ""
        if not res:
            res = [-1, -1]
        elif len(res) == 1:
            res.append(res[0])
        elif len(res) > 2:
            # print([res[0], res[len(res)-1]])
            return [res[0], res[len(res)-1]]

        # print(res)
        return res

x = Solution()

nums = [5,7,7,8,8,10]
target = 8
x.searchRange(nums, target)

nums = [5,7,7,8,8,10]
target = 6
x.searchRange(nums, target)

nums = [1,1,1,1,1,1,1]
target = 1
x.searchRange(nums, target)

nums = [1]
target = 1
x.searchRange(nums, target)