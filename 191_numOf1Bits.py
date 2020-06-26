class Solution:
    def hammingWeight(self, n: int) -> int:
        print(bin(n)[2:].count('1'))
        
X = Solution()

n = 00000000000000000000000000001011
X.hammingWeight(n)

n = 00000000000000000000000010000000
X.hammingWeight(n)

n = 11111111111111111111111111111101
X.hammingWeight(n)