class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n:
            zeros += n // 5
            n //= 5
        print(zeros)
        return zeros

X = Solution()

n = 3
X.trailingZeroes(n)

n = 5
X.trailingZeroes(n)

n = 0
X.trailingZeroes(n)