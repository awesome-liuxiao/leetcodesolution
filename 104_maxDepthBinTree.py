# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        
        return max(left, right)
        
X = Solution()

root = TreeNode()
root.val = 3
root.left = TreeNode()
root.left.val = 9
root.right = TreeNode()
root.right.val = 20
root.right.left = TreeNode()
root.right.left.val = 15
# root.right.right = TreeNode()
# root.right.right.val = 7
print(X.maxDepth(root))