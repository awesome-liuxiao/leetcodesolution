class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = s[0]
        cntNum = 1
        res = 0
        for i in range(1, len(s)):
            if s[i] == prev:
                cntNum += 1
            else:
                j = i
                while cntNum > 0 and j < len(s):
                    # print(f"cntNum: {cntNum}")
                    # print(f"j: {j}, s[j]: {s[j]}")
                    if s[j] != prev:
                        res += 1
                        cntNum -= 1
                        # print(f"cntNum: {cntNum}")
                    else:
                        break
                    j += 1
                prev = s[i]
                cntNum = 1
        print(res)
        return res


X = Solution()

s = "00110011"
X.countBinarySubstrings(s)

s = "10101"
X.countBinarySubstrings(s)