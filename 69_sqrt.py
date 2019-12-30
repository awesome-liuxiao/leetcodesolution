class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        l = 1
        r = x
        res = 0
        while l <= x:
            res = (l+r) // 2
            s = res ** 2
            if s <= x < (res+1)**2:
                # print(res)
                return res
            if s < x:
                l = res
            if s > x:
                r = res

        
main = Solution()

x = 4
main.mySqrt(x)

x = 8
main.mySqrt(x)