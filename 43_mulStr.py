class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = ""
        intNum1 = 0
        intNum2 = 0
        place = 0
        for i in range(len(num1)):
            intNum1 += int(num1[len(num1)-1-i]) * pow(10,place)
            place += 1
        place = 0
        for i in range(len(num2)):
            intNum2 += int(num2[len(num2)-1-i]) * pow(10,place)
            place += 1

        res = str(intNum1*intNum2)
        # print(res)
        return res


        
x = Solution()

num1 = "2"
num2 = "3"
x.multiply(num1, num2) # 6

num1 = "123"
num2 = "456"
x.multiply(num1, num2) #56088

num1 = "0"
num2 = "123"
x.multiply(num1, num2) # 0