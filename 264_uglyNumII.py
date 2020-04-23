class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dpList = [1]*n
        p2, p3, p5 = 0, 0, 0
        for i in range(1,n):
            cur = min(2*dpList[p2], 3*dpList[p3], 5*dpList[p5])
            if cur == 2*dpList[p2]:
                p2 += 1
            if cur == 3*dpList[p3]:
                p3 += 1
            if cur == 5*dpList[p5]:
                p5 += 1
            dpList[i] = cur
        print(dpList[n-1])
        return dpList[n-1]
        
X = Solution()

n = 10
X.nthUglyNumber(n)

n = 1
X.nthUglyNumber(n)

n = 1690
X.nthUglyNumber(n)