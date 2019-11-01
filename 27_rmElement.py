from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0 # a pointer to mark position
        while p < len(nums): # if the pointer reached the boundary, end
            if nums[p] == val:
                nums.pop(p) # if same, pop out the element, the pointer's position doesn't change.
            else:
                p += 1 # if not same, then the pointer move to next element
        return len(nums)

x = Solution()
nums1 = [3,2,2,3]
val1 = 3
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
nums3 = [1,1,1]
val3 = 1
nums4 = [1]
val4 = 1
nums5 = []
val5 = 0

print(x.removeElement(nums1, val1))
print(x.removeElement(nums2, val2))
print(x.removeElement(nums3, val3))
print(x.removeElement(nums4, val4))
print(x.removeElement(nums5, val5))