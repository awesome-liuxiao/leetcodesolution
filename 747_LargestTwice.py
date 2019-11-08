from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        res = -1
        if len(nums) < 1:
            return res
        if len(nums) == 1: # if there is only one element in nums, then itself is the largest
            return 0
        '''
        the main idea of this is sort and reverse a new list, if the the largest element is equal or bigger than the twice of the second element, then it is twice larger than all of the rest, therefore, it is the largest; otherwise, no largest can be found.
        '''
        tmpList = nums.copy()
        tmpList.sort()
        tmpList.reverse()
        largestIdx = nums.index(tmpList[0])
        if tmpList[0] >= tmpList[1]*2:
            res = largestIdx

        # print(res)
        return res



x = Solution()

nums = [3, 6, 1, 0]
x.dominantIndex(nums)

nums = [1, 2, 3, 4]
x.dominantIndex(nums)

nums = [1]
x.dominantIndex(nums)