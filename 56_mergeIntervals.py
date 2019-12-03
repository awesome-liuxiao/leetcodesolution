from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        flag = 0
        if not intervals:
            return
        intervals.sort()
        res = [intervals[0]]
        # print("intervals: ", end="")
        # print(intervals)
        if len(intervals) == 1:
            res = intervals
        for i in range(1, len(intervals)):
            x = 0
            y = 0
            lx = res[-1]
            ly = intervals[i]
            # print("lx: ",end="")
            # print(lx)
            # print("ly: ",end="")
            # print(ly)
            if (lx[1] >= ly[0]):
                res.pop()
                x = min(lx[0], ly[0])
                y = max(lx[1], ly[1])
                res.append([x,y])
            else:
                res.append(ly)
            flag += 1
            # print("res: ",end="")
            # print(res)
        print(res)
        return res

x = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
x.merge(intervals)

intervals = [[1,4],[4,5]]
x.merge(intervals)

intervals = [[]]
x.merge(intervals)

intervals = [[1,2]]
x.merge(intervals)

intervals = [[1,4],[0,4]]
x.merge(intervals)

intervals = [[1,3],[2,6],[8,10],[15,18],[17,20]]
x.merge(intervals)

intervals = [[1,4],[0,0]]
x.merge(intervals)

intervals = [[1,4],[0,2],[3,5]]
x.merge(intervals)

intervals = []
x.merge(intervals)