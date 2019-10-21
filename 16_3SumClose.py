from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        nums.sort()
        res = float('inf')
        for i in range(length):
            left = i + 1
            right = length - 1
            while left < right:
                tmpSum = nums[left]+nums[i]+nums[right]
                if abs(tmpSum - target) < abs(res - target):
                    res = tmpSum
                if tmpSum < target:
                    left += 1
                else:
                    right -= 1
        return res

x = Solution()
data1 = [-1, 2, 1, -4]
print(x.threeSumClosest(data1, 1))