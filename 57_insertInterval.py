from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        flag = 0
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals[0]]
        if len(intervals) == 1:
            res = intervals
        for i in range(1, len(intervals)):
            x = 0
            y = 0
            lx = res[-1]
            ly = intervals[i]
            if (lx[1] >= ly[0]):
                res.pop()
                x = min(lx[0], ly[0])
                y = max(lx[1], ly[1])
                res.append([x,y])
            else:
                res.append(ly)
            flag += 1
        # print(res)
        return res

x = Solution()

intervals = [[1,3],[6,9]]
newInterval = [2,5]
# x.insert(intervals, newInterval)

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
# x.insert(intervals, newInterval)

intervals = [[1,5]]
newInterval = [0,3]
x.insert(intervals, newInterval)


intervals = []
newInterval = [0,3]
x.insert(intervals, newInterval)