import itertools
class Solution:
    def getPermutation(self, n: int, k: int) -> str: 
        lset = []
        res = ""
        for i in range(1,n+1):
            lset.append(i)
        permuls = list(itertools.permutations(lset,n))
        for e in permuls[k-1]:
            res += str(e)
        print(res)
        return res

x = Solution()

n = 3
k = 3
x.getPermutation(n,k)

n = 4
k = 9
x.getPermutation(n,k)

n = 1
k = 1
x.getPermutation(n,k)