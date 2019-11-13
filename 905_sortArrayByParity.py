from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for n in A:
            if n % 2 == 0:
                odd.append(n)
            else:
                even.append(n)
        # print(odd+even)
        return odd + even
        
x = Solution()

A = [3,1,2,4]
x.sortArrayByParity(A)

A = []
x.sortArrayByParity(A)
