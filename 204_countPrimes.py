class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [False,False] + [True]*(n-2)
        primeCnt = 0
        for i in range(2,n):
            if primes[i]:
                for j in range(i+i,n,i):
                    primes[j] = False
        print(sum(primes))
        return sum(primes)

        
X = Solution()

n = 10
X.countPrimes(n)