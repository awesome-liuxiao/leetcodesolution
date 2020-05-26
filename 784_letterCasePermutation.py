from typing import List
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        def permute(S, substring, index):
            if len(substring) == len(S):
                res.append(substring)
                return
            if S[index].isalpha():
                permute(S, substring+S[index].lower(), index+1)
                permute(S, substring+S[index].upper(), index+1)
            else:
                permute(S, substring+S[index], index+1)
        permute(S, '', 0)
        # print(res)
        return res

X = Solution()

S = "a1b2"
X.letterCasePermutation(S)

S = "3z4"
X.letterCasePermutation(S)

S = "12345"
X.letterCasePermutation(S)