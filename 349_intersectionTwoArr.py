from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n in nums1:
            if (n in nums2) and (not n in res):
                res.append(n)
        print(res)
        return res


x = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]
x.intersection(nums1,nums2)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
x.intersection(nums1,nums2)
