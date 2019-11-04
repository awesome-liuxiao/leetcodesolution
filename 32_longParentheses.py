class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        sLen = len(s)
        stack = []
        start = 0
        for i in range(sLen):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack == []:
                    start = i+1
                else:
                    stack.pop()
                    if stack == []:
                        res = max(res, i-start+1)
                    else:
                        res = max(res, i - stack[len(stack)-1])
        # print(res)
        return res

x = Solution()
data1 = "(()" # 2
# data2 = ")()())" # 4
data3 = "()(()" # 2
data4 = "(((())))" # 8
# x.longestValidParentheses(data1)
# x.longestValidParentheses(data2)
x.longestValidParentheses(data3)
# x.longestValidParentheses(data4)
