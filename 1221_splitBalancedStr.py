class Solution:
    def balancedStringSplit(self, s: str) -> int:
        numOfL = 0
        numOfR = 0
        res = []
        tmp = ""
        for c in s:
            tmp += c
            if c == "L":
                numOfL += 1
                if numOfL == numOfR:
                    res.append(tmp)
                    tmp = ""
                    numOfL = 0
                    numOfR = 0
            else:
                numOfR += 1
                if numOfR == numOfL:
                    res.append(tmp)
                    tmp = ""
                    numOfL = 0
                    numOfR = 0
        # print(res)
        return len(res)


x = Solution()

s = "RLRRLLRLRL"
x.balancedStringSplit(s)

s = "RLLLLRRRLR"
x.balancedStringSplit(s)

s = "LLLLRRRR"
x.balancedStringSplit(s)

s = "RLRRRLLRLL"
x.balancedStringSplit(s)