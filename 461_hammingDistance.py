class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        ones = 0
        while num:
            # print(num)
            if num & 1 == 1:
                ones += 1
            num = num >> 1

        # print(ones)
        return ones

p = Solution()

x = 1
y = 4
p.hammingDistance(x,y) #2

x = 101
y = 24
p.hammingDistance(x,y) #2

x = 0
y = 500
p.hammingDistance(x,y) #2