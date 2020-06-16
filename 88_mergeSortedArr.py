from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        for i in range(m, m+n):
            nums1[i] = nums2[j]
            j += 1
        if len(nums1) == m + n:
            nums1.sort()
        else:
            nums1[:m+n].sort()
        print(nums1)
        """
        Do not return anything, modify nums1 in-place instead.
        """
    
X = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
X.merge(nums1, m, nums2, n)

nums1 = [1,0]
m =1
nums2 = [0]
n = 1
X.merge(nums1, m, nums2, n)