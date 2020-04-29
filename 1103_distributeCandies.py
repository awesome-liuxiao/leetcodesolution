from typing import List
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0]*num_people
        if num_people == 1:
            res[0] = candies
            print(res)
            return res
        else:
            res[0] = 1
            candies -= 1
            turn = 0
            i = 1
        while candies > 0:
            if candies >= i+1 + num_people*turn:
                addCandies = i+1 + num_people*turn
                res[i] += addCandies
                candies -= addCandies
            else:
                res[i] += candies
                candies = 0
            # print("res: "+str(res) + ", candies: " + str(candies) + ", i: " + str(i))
            if i == num_people - 1:
                i = 0
                turn += 1
            else:
                i += 1
        print(res)
        return res

X = Solution()

candies = 7
num_people = 4
X.distributeCandies(candies, num_people)

candies = 10
num_people = 3
X.distributeCandies(candies,num_people)

candies = 30
num_people = 3
X.distributeCandies(candies,num_people)

candies = 100
num_people = 1
X.distributeCandies(candies,num_people)