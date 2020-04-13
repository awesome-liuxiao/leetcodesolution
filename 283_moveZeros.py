from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        flag = 0
        numsLen = len(nums)
        while flag < numsLen:
            if nums[idx] == 0:
                del nums[idx]
                nums.append(0)
            else:
                idx += 1
            flag += 1
        # print(nums)

x = Solution()

nums = [0,1,0,3,12]
x.moveZeroes(nums)

nums = [1,2,0,3,0]
x.moveZeroes(nums)

nums = [0,0,1,0]
x.moveZeroes(nums)

nums = [0,1]
x.moveZeroes(nums)

nums = [0]
x.moveZeroes(nums)