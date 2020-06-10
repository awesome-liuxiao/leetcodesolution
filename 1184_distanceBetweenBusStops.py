from typing import List
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        cur = start
        rightMiles = 0
        leftMiles = 0
        while cur != destination:
            # if cur == len(distance) - 1:
            #     cur == -1
            # print(f"cur: {cur}")
            rightMiles += distance[cur]
            # print(f"rightMiles: {rightMiles}")
            if cur == len(distance) - 1:
                cur = 0
            else:
                cur += 1
        # print(f"rightMiles: {rightMiles}")
        cur = start
        while cur != destination:
            # print(f"cur: {cur}")
            leftMiles += distance[cur - 1]
            # print(leftMiles)
            if cur == 0:
                cur = len(distance) - 1
            else:
                cur -= 1
        # print(f"leftMiles: {leftMiles}")

        # print(min(rightMiles, leftMiles))
        return min(rightMiles, leftMiles)
        
X = Solution()

distance = [1,2,3,4]
start = 0
destination = 1
X.distanceBetweenBusStops(distance, start, destination)

distance = [1,2,3,4]
start = 0
destination = 2
X.distanceBetweenBusStops(distance, start, destination)

distance = [1,2,3,4]
start = 3
destination = 1
X.distanceBetweenBusStops(distance, start, destination)
