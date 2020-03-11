from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        numLen = len(nums)
        for i in range(numLen):
            res.append(0)
            for j in range(numLen):
                if j != i:
                    if nums[j] < nums[i]:
                        res[i] += 1
        print(res)
        return res

x = Solution()

nums = [8,1,2,2,3] #[4,0,1,1,3]
x.smallerNumbersThanCurrent(nums)

nums = [6,5,4,8] #[2,1,0,3]
x.smallerNumbersThanCurrent(nums)

nums = [7,7,7,7] #[0,0,0,0]
x.smallerNumbersThanCurrent(nums)

nums = [0]
x.smallerNumbersThanCurrent(nums)

nums = [1,0,0]
x.smallerNumbersThanCurrent(nums)

nums = [-1,2,3,-5,6]
x.smallerNumbersThanCurrent(nums)
