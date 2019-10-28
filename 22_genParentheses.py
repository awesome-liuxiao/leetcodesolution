from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]: 
        res = []
        out = ""

        def backtrack(left: int, right: int, out: str, res: List[str]):
            # print("out: "+out)
            if left > right:
                return
            if left == 0 and right == 0:
                # print("append")
                res.append(out)
            else:
                if left > 0:
                    #out += '(' # wrong operation
                    # print('left: '+str(left))
                    backtrack(left-1, right, out+'(', res)
                if right > left:
                    #out += ')' # wrong operation
                    # print('right: '+ str(right))
                    backtrack(left, right-1, out+')', res)
        backtrack(n, n, out, res)
        return res
        
x = Solution()            
print(x.generateParenthesis(3))