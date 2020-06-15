from typing import List
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        allSum = sum(A)
        if allSum % 3 != 0: # cannot be 3 parts
            return False
        sum1 = allSum/3
        sum2 = 0
        indicator = 0
        for i in range(len(A)):
            sum2 += A[i]
            if sum1 == sum2:
                sum2 = 0
                indicator += 1
            if indicator == 2 and i < len(A)-1:
                return True
        return False
        # i = 1
        # while i < len(A) - 1:
        #     sum1 = 0
        #     sum2 = 0
        #     sum3 = 0
        #     sum1 = sum(A[0:i])
        #     for j in range(i,len(A)-1):
        #         sum2 += A[j]
        #         if sum2 == sum1:
        #             for k in range(j+1, len(A)):
        #                 sum3 += A[k]
        #             if sum2 == sum3:
        #                 return True
        #     i += 1
        # return False
        
X = Solution()

A = [0,2,1,-6,6,-7,9,1,2,0,1]
print(X.canThreePartsEqualSum(A))

A = [0,2,1,-6,6,7,9,-1,2,0,1]
print(X.canThreePartsEqualSum(A))

A = [3,3,6,5,-2,2,5,1,-9,4]
print(X.canThreePartsEqualSum(A))

# print()
A = [18,12,-18,18,-19,-1,10,10]
print(X.canThreePartsEqualSum(A))

A = [1,-1,1,-1]
print(X.canThreePartsEqualSum(A))

import random
nums = []
for i in range(50000):
    nums.append(random.choice([pow(-10,4),pow(10,4)]))
# print(nums)
# print(X.canThreePartsEqualSum(nums))
