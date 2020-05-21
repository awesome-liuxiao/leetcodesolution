from typing import List
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sumOfEven = sum([n for n in A if n % 2 == 0])
        for query in queries:
            val, idx = query
            if val % 2 == 0 and A[idx] % 2 == 0:
                sumOfEven += val
            if val % 2 == 0 and A[idx] % 2 == 1:
                pass
            if val % 2 == 1 and A[idx] % 2 == 1:
                sumOfEven += val + A[idx]
            if val % 2 == 1 and A[idx] % 2 == 0:
                sumOfEven -= A[idx]
            A[idx] += val
            # print(A,end="sumOfEven: ")
            # print(sumOfEven)
            res.append(sumOfEven)
        print(res)
        return res
        

X = Solution()

A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
X.sumEvenAfterQueries(A, queries)