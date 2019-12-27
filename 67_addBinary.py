class Solution:
    def addBinary(self, a: str, b: str) -> str:
       # print(bin(int(a,2)+int(b,2))[2:])
       return bin(int(a,2)+int(b,2))[2:]

x = Solution()

a = "11"
b = "1"
x.addBinary(a,b)

a = "1010"
b = "1011"
x.addBinary(a,b)

a = "1"
b = "0"
x.addBinary(a,b)