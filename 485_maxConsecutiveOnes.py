from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        onesList = []
        ones = 0
        for n in nums:
            if n == 1:
                ones += 1
                # print(ones)
            else:
                onesList.append(ones)
                ones = 0
        onesList.append(ones)
        print(max(onesList))
        return max(onesList)
        
X = Solution()

nums = [1,1,0,1,1,1]
X.findMaxConsecutiveOnes(nums)

import random
nums = []
for i in range(10000):
    nums.append(random.choice([0,1]))
print(nums)
print(len(nums))
X.findMaxConsecutiveOnes(nums)