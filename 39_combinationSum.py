from typing import List
class Solution:
    def combinationSum(self, candidates:List[int], target:int) -> List[List[int]]:
        res = []
        def findDFS(candidates, target, start, out, res):
            if target < 0:
                return
            elif target == 0:
                res.append(out)
                return
            for i in range(start, len(candidates)):
                out.append(candidates[i])
                findDFS(candidates, target - candidates[i], i, out, res)
                out.pop(len(out)-1) # backtracking
        findDFS(candidates, target, 0, [], res)
        # print(res)
        return res

        

x = Solution()

candidates = [2,3,6,7]
target = 7
x.combinationSum(candidates, target)

# candidates = [2,3,5]
# target = 8
# x.combinationSum(candidates, target)