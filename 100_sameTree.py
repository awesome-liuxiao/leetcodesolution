# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def fn(p, q): 
            """Return True if trees rooted at p and q are structurally identical"""
            if not p or not q: return p is q
            return fn(p.left, q.left) and p.val == q.val and fn(p.right, q.right)
        
        return fn(p, q)

X = Solution()

t1 = TreeNode()
t1.val = 1
t1.left = 2
t1.right = 3
t2 = TreeNode()
t2.val = 1
t2.left = 2
t2.right = 3
print(X.isSameTree(t1, t2))

t3 = TreeNode()
t3.val = 1
t3.left = 2
t4 = TreeNode()
t4.val = 1
t4.right = 2
print(X.isSameTree(t3, t4))

t5 = TreeNode()
t5.val = 1
t5.left = 2
t5.right = 1
t6 = TreeNode()
t6.val = 1
t6.left = 1
t6.right = 2
print(X.isSameTree(t5, t6))
