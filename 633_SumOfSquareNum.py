import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        res = 0
        a= 0
        b = int(math.sqrt(c))
        isSquare = False
        # if c == 0:
        #     isSquare = True
        while a <= b: # a should always be equal or less than b, therefore to make the a^2 + b^2 = c.
            res = a*a + b*b
            print('a: '+str(a)+', b: '+str(b)+', res: '+str(res))
            if res == c:
                isSquare = True
                break
            elif res > c:
                b -= 1
            else:
                a += 1
        print(isSquare)
        return isSquare

X = Solution()

# c = 5
# X.judgeSquareSum(c)

# c = 3
# X.judgeSquareSum(c)

c = 300
X.judgeSquareSum(c)