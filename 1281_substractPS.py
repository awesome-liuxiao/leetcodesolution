class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nStr = str(n)
        sumN = int(nStr[0])
        productN = int(nStr[0])
        for i in nStr[1:]:
            sumN += int(i)
            productN *= int(i)
        # print(str(productN)+"-"+str(sumN)+"="+str(productN-sumN))
        return productN-sumN
        

x = Solution()

n = 234
x.subtractProductAndSum(n)

n = 4421
x.subtractProductAndSum(n)

n = 1
x.subtractProductAndSum(n)

n = 100
x.subtractProductAndSum(n)