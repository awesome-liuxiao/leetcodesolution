class Solution:
    def convert(self, s: str, numRows: int):
        if numRows == 1:
            return s
        line = 0
        step = 1
        arr = [""]*numRows
        for c in s:
            if line == 0:
                step = 1
            elif line == numRows - 1:
                step = -1
            arr[line] += c
            line += step
        return "".join(arr)





# x = Solution()
# print(x.convert("PAYPALISHIRING",4))


"""
PAYPALISHIRING
4
P     I    N
A   L S  I G
Y A   H R
P     I
"""