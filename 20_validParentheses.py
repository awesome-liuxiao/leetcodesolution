class Solution:
    def isValid(self, s: str) -> bool:
        if s == [] or len(s) == 1 or len(s) % 2 == 1:
            return False
        stack = []
        left = ['(','[','{']
        right = [')',']','}']
        for e in s:
            if e in left:
                stack.append(e)
            elif e in right:
                if e == ')' and '(' in stack:
                    stack.pop()
                if e == ']' and '[' in stack:
                    stack.pop()
                if e == '}' and '{' in stack:
                    stack.pop()
        if stack == []:
            return True
        else:
            return False

x = Solution()
data1 = "()"
data2 = "()[]{}"
data3 = "(]"
data4 = "([)]"
data5 = "{[]}"

print(x.isValid(data1))
print(x.isValid(data2))
print(x.isValid(data3))
print(x.isValid(data4))
print(x.isValid(data5))
