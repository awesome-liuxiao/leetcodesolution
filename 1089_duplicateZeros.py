from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if len(arr) <= 1:
            return
        i = 0 # a pointer to record the traversing position
        while i<len(arr)-1:
            if arr[i] == 0:
                tmp1 = arr[0:i]
                tmp2 = arr[i+1:] # cutting the array as two parts: before and after zero
                for j in range(len(tmp1)):
                    arr[j] = tmp1[j] # since the elements before 0 don't change, then keep them in the array.
                arr[i+1] = 0 # set the element right after zero as 0.
                i += 2 # move the pointer after the newly setted zero
                m = 0 # counter for tmp2
                for k in range(i, len(arr)):
                    arr[k] = tmp2[m] # put the remained elements into array start from pointer to end.
                    m += 1
            else:
                i += 1 # if there is no zero in this round, then move pointer to next.
            # print(arr)

        print(arr)

x = Solution()

arr = [1,0,2,3,0,4,5,0]
x.duplicateZeros(arr)

arr = [1,2,3]
x.duplicateZeros(arr)

arr = [0]
x.duplicateZeros(arr)

arr = [0,0,0,0,0,0,1]
x.duplicateZeros(arr)