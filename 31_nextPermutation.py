from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hasPernutaion = False
        p = 0
        i = len(nums)-1
        while i > 0:
            if nums[i] > nums[i-1]:
                hasPernutaion = True
            j = len(nums) - 1
            while j > i - 1:
                if nums[j] > nums[i-1]:
                    tmp = nums[i-1]
                    nums[i-1] = nums[j]
                    nums[j] = tmp
                    # print('swaped first')
                    # print(nums)
                    break
                j -= 1
            if hasPernutaion:
                break
            else:
                i -= 1
        # print(i)
        if hasPernutaion:
            # print("here")
            # for k in range(i, len(nums)-1):
            #     for l in range(i+1, len(nums)):
            #         if nums[k] > nums[l]:
            #             tmp = nums[l]
            #             nums[l] = nums[k]
            #             nums[k] = tmp
            #             print(nums)
            nums[i:] = sorted(nums[i:])
        else:
            nums.sort()
        # print('----res------')
        # print(nums)




data1 = [1,2,3]
data2 = [3,2,1]
data3 = [1,1,5]
data4 = [6,8,7,4,3,2]
data5 = [1,3,2] # 2,1,3
x = Solution()
x.nextPermutation(data4)
        