from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n in nums1:
            if n in nums2:
                res.append(n)
                # del nums1[nums1.index(n)]
                del nums2[nums2.index(n)]
        print(res)
        return res

X = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]
X.intersect(nums1, nums2)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
X.intersect(nums1, nums2)

nums1 = [4,9,5]
nums2 = [4,4,4]
X.intersect(nums1, nums2)