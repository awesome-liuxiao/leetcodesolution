from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        roomNum = len(rooms)
        if not rooms:
            return False
        stack = rooms[0]
        seen = set([0])

        while stack:
            key = stack.pop()
            if key not in seen:
                seen.add(key)
                for nxt in rooms[key]:
                    if nxt not in seen:
                        stack.append(nxt)
        return len(seen) == roomNum

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