from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        numsSet = sorted(list(set(nums)))
        # print(nums)
        # print(numsSet)
        missing = 1
        for n in numsSet:
            # print("n: "+str(n))
            if n > 0:
                if n == missing:
                    missing += 1
                    # print("missing: "+str(missing))
                    continue
                else:
                    break
        # print(missing)
        return missing

x = Solution()

# nums = [1,2,0] # 3
# x.firstMissingPositive(nums)

# nums = [3,4,-1,1] # 2
# x.firstMissingPositive(nums)

# nums = [7,8,9,11,12] # 1
# x.firstMissingPositive(nums)

# nums = [0]
# x.firstMissingPositive(nums)

# nums = [0,2,2,1,1] # 3
# x.firstMissingPositive(nums)

nums = [1, 1000]
x.firstMissingPositive(nums)