from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {'2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_nums):
            if len(next_nums) == 0:
                res.append(combination)
            else:
                for letter in nums[next_nums[0]]:
                    # print("letter: "+letter)
                    # print("combination: "+combination)
                    backtrack(combination+letter, next_nums[1:])

        res = []
        if digits != "":
            backtrack("", digits)
        return res

x = Solution()
print(x.letterCombinations("23"))