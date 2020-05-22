class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        else:
            return self.fib(N-1)+self.fib(N-2)
        
X = Solution()

N = 2
print(X.fib(N))


N = 3
print(X.fib(N))

N = 4
print(X.fib(N))