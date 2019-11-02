class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            k = 0
            tmp = divisor
            while dividend >= tmp:
                dividend -= tmp
                quotient += 1 << k
                tmp <<= 1
                k += 1

        if quotient > MAX_INT and sign > 0:
            quotient = MAX_INT
        if sign < 0:
            quotient = 0 - quotient
        print(quotient)
        return quotient

x = Solution()
x.divide(10, 3)
x.divide(7, -3)
x.divide(-1 , -1)
x.divide(-1 , 1)
x.divide(-2147483648, -1)
x.divide(-2147483648, 1)
x.divide(2147483647, 2)