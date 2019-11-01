from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 1 # two nested points
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        while p2 > 0:
            # print("nums["+str(p1)+"]: "+ str(nums[p1])+", nums["+str(p2)+"]: "+str(nums[p2]))
            if nums[p1] == nums[p2]:
                # print("popping")
                nums.pop(p1)
            else:
                # print("moving")
                p1 += 1
                p2 += 1
            if p2 > len(nums)-1:
                # print("breaking")
                p2 = -1
            # print(nums)
        return len(nums)

nums1 = [1,1,3]
nums2 = [0,0,1,1,1,2,2,3,3,4]
nums3 = [1,1]
nums4 = [1]
nums5 = []
nums6 = [1,1,1]
nums7 = [-1,0,0,0,0,3,3]

x = Solution()
print(x.removeDuplicates(nums1))
print(x.removeDuplicates(nums2))
print(x.removeDuplicates(nums3))
print(x.removeDuplicates(nums4))
print(x.removeDuplicates(nums5))
print(x.removeDuplicates(nums6))
print(x.removeDuplicates(nums7))