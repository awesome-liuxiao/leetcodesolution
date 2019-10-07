class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        theList = nums1 + nums2
        theList.sort()
        lenOfList = len(theList)
        if lenOfList % 2 == 0:
            mid =float( (theList[int(lenOfList/2)] + theList[int(lenOfList/2 -1)]) / 2)
        else:
            mid = float(theList[int(lenOfList/2)])
        return mid

x = Solution()
# nums1 = [1, 3]
# nums2 = [2]

nums1 = [1, 2]
nums2 = [3, 4]
print(x.findMedianSortedArrays(nums1, nums2))
