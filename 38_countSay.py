class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        i = 1
        while i < n:
            tmp = res
            res = ""
            count = 1
            j = 0
            for j in range(len(tmp)):
                if j+1 < len(tmp) and tmp[j] == tmp[j+1]:
                    count += 1
                else:
                    res += str(count) + tmp[j]
                    count = 1
            i += 1
        # print(res)
        return res

x = Solution()
x.countAndSay(4)
x.countAndSay(6) # 312211
x.countAndSay(10) # 13211311123113112211