from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numAndOccur = {}
        occurs = set()
        for n in arr:
            if n not in numAndOccur:
                numAndOccur[n] = 1
            else:
                numAndOccur[n] += 1
        for m in numAndOccur:
            occurs.add(numAndOccur[m])
        if len(numAndOccur) == len(occurs):
            return True
        return False

X = Solution()

arr = [1,2,2,1,1,3]
print(X.uniqueOccurrences(arr))

arr = [1,2]
print(X.uniqueOccurrences(arr))

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(X.uniqueOccurrences(arr))