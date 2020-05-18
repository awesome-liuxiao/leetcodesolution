from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for n in arr2:
            while n in arr1:
                res.append(n)
                del arr1[arr1.index(n)]
        res += sorted(arr1)
        print(res)
        return res

X = Solution()

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
X.relativeSortArray(arr1, arr2)