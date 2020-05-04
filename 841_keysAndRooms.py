from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        res = False
        keys = []
        roomNum = 0
        if not rooms[0]:
            return res
        for room in rooms:
            if not room:
                roomNum += 1
                continue
            for key in room:
                if (key not in keys) and (roomNum != key):
                    keys.append(key)
            roomNum += 1
        keys.sort()
        if keys[0] == 0:
            del keys[0]
        print(keys)
        if :
            pass
        for i in range(1,len(rooms)):
            if i == keys[i-1]:
                res = True
            else:
                res = False
                break
        print(res)
        return res

X = Solution()

rooms = [[1],[2],[3],[]] #True
X.canVisitAllRooms(rooms)

rooms = [[1,3],[3,0,1],[2],[0]] #False
X.canVisitAllRooms(rooms)

rooms = [[3],[2],[],[1]] #True
X.canVisitAllRooms(rooms)

rooms = [[1],[],[3],[2],[1]] #False
X.canVisitAllRooms(rooms)

rooms = [[2],[2],[1,1],[3]]
X.canVisitAllRooms(rooms)