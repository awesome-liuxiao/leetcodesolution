from typing import List
import collections
class Solution:
    def combinationSum2(self, candidates:List[int], target:int) -> List[List[int]]:
        res = []
        candidatesCounter = collections.Counter(candidates)
        self.findDFS(candidates, candidatesCounter, target, 0, [], res)
        # print(res)
        return res

    def findDFS(self, candidates, candidatesCounter, target, start, out, res):
        if target < 0:
            return
        if target == 0:
            isRepeat = False
            outCounter = collections.Counter(out)
            for e in out:
                if outCounter[e] > candidatesCounter[e]:
                    isRepeat = True
            if not isRepeat:
                out.sort()
                if out not in res:
                    res.append(out)
            return
        for i in range(start, len(candidates)):
            # candidates.pop(i)
            self.findDFS(candidates, candidatesCounter, target-candidates[i],i,out+[candidates[i]],res)



x = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
x.combinationSum2(candidates, target)

# candidates = [2,5,2,1,2]
# target = 5
# x.combinationSum2(candidates, target)