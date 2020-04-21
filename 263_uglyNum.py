class Solution:
    def isUgly(self, num: int) -> bool:
        while num > 1 and (num % 2 == 0):
            num /= 2
        while  num > 1 and (num % 3 == 0):
            num /= 3
        while  num > 1 and (num % 5 == 0):
            num /= 5
        if num == 1:
            print("True")
            return True
        else:
            print("False")
            return False
X = Solution()

num = 6
X.isUgly(num)

num = 14
X.isUgly(num)