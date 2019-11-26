class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        half = self.myPow(x, int(n/2))
        if n % 2 == 0:
            return half*half
        if n > 0:
            return half*half*x
        return half * half/x

a = Solution()

x = 2.00000
n = 10
print(a.myPow(x,n))

x = 2.10000
n = 3
print(a.myPow(x,n))

x = 2.00000
n = -2
print(a.myPow(x,n))

x = 0.00001
n = 2147483647
print(a.myPow(x,n))