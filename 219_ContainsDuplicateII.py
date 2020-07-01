from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, i+k+1):
                if i != j and j < len(nums) and nums[i] == nums[j]:
                    return True

        return False

X = Solution()

nums = [1,2,3,1]
k = 3
print(X.containsNearbyDuplicate(nums, k))

nums = [1,0,1,1]
k = 1
print(X.containsNearbyDuplicate(nums, k))

nums = [1,2,3,1,2,3]
k = 2
print(X.containsNearbyDuplicate(nums, k))

nums = []
k = 2
print(X.containsNearbyDuplicate(nums, k))

