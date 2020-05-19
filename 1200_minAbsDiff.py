from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr.sort()
        flag = []
        minDiff = abs(arr[0]-arr[-1])
        for i in range(len(arr)-1):
            diff = abs(arr[i]-arr[i+1])
            if diff < minDiff:
                if not res:
                    minDiff = diff
                    res.append([arr[i],arr[i+1]])
                else:
                    res = []
                    minDiff = diff
                    res.append([arr[i],arr[i+1]])
            elif diff == minDiff:
                res.append([arr[i],arr[i+1]])
        print(res)
        return res


X = Solution()

arr = [4,2,1,3]
X.minimumAbsDifference(arr)

arr = [1,3,6,10,15]
X.minimumAbsDifference(arr)

arr = [3,8,-10,23,19,-4,-14,27]
X.minimumAbsDifference(arr)

arr = [40,11,26,27,-20]
X.minimumAbsDifference(arr)