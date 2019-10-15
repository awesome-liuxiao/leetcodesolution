class Solution:
    def intToRoman(self, num: int) -> str:
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'] # 0,1,2,3,4,5,6,7,8,9
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'] # 0,10,20,30,40,50,60,70,80,90
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'] # 0,100,200,300,400,500,600,700,800,900
        M = ['', 'M', 'MM', 'MMM'] # 0,1000,2000,3000
        res = M[num // 1000] + C[(num%1000) // 100] + X[(num%100) // 10] + I[num%10]
        return res

x = Solution()
print(x.intToRoman(3))
print(x.intToRoman(4))
print(x.intToRoman(9))
print(x.intToRoman(58))
print(x.intToRoman(1994))
print(x.intToRoman(1))
print(x.intToRoman(3999))