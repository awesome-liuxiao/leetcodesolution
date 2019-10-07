class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for num in nums:
            tmp = target - num
            try:
                j = nums.index(tmp)
                if (tmp in nums) and (j != i):
                    if i < j:
                        return([i,j])
                    else:
                        return([j,i])
            except ValueError as err:
                pass
            i += 1
