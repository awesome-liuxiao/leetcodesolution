# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return root1.val == root2.val and dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        if root:
            return dfs(root.left, root.right)
        return True
X = Solution()

root = TreeNode()
root.val = 1
root.left = TreeNode()
root.left.val = 2
root.left.left = TreeNode()
root.left.left.val = 3
root.left.right = TreeNode()
root.left.right.val = 4
root.right = TreeNode()
root.right.val = 2
root.right.left = TreeNode()
root.right.left.val = 4
root.right.right = TreeNode()
root.right.right.val = 3
print(X.isSymmetric(root))

root = TreeNode()
root.val = 1
root.left = TreeNode()
root.left.val = 2
root.left.right = TreeNode()
root.left.right.val = 3
root.right = TreeNode()
root.right.val = 2
root.right.right = TreeNode()
root.right.right.val = 3
print(X.isSymmetric(root))
        