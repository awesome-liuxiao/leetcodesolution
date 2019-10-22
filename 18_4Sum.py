from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        length = len(nums)
        nums.sort()
        for i in range(length):
            for j in range(i+1, length):
                left = j + 1
                right = length - 1
                while left < right:
                    # print("++++++++++++++")
                    # print(i)
                    # print(j)
                    # print(left)
                    # print(right)
                    # print("++++++++++++++")
                    tmpSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmpSum == target:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif tmpSum < target:
                        left += 1
                    else:
                        right -= 1
        return res

x = Solution()
data = [1, 0, -1, 0, -2, 2]
print(x.fourSum(data, 0))