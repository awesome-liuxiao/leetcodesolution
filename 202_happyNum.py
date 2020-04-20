class Solution:
    def calSumSquare(self,num):
        tmpSum = 0
        for e in num:
            tmpSum += pow(int(e),2)
        return tmpSum
    def isHappy(self, n: int) -> bool:
        sums = []
        nStr = str(n)
        theSum = 0
        happy = False
        while True:
            theSum = self.calSumSquare(nStr)
            if theSum == 1:
                happy = True
                break
            else:
                if theSum in sums:
                    happy = False
                    break
                else:
                    sums.append(theSum)
                    nStr = str(theSum)
        print(happy)
        return happy

X = Solution()

n = 19
X.isHappy(n)

n = 210
X.isHappy(n)