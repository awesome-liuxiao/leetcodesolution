# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        range_sum = self.getRangeSum(root, L, R)
        print(range_sum)
        return range_sum

    def getRangeSum(self, node, L, R):
        if not node:
            return 0
        if node.val > R:
            range_sum = self.getRangeSum(node.left, L, R)
        elif node.val < L:
            range_sum = self.getRangeSum(node.right, L, R)
        else:
            range_sum = node.val + self.getRangeSum(node.left, L, R) + self.getRangeSum(node.right, L, R)
        return range_sum
        

x = Solution()

nodeList = [10,5,15,3,7,0,18] #7
root = TreeNode(nodeList[0])
root.left = TreeNode(nodeList[1])
root.right = TreeNode(nodeList[2])
root.left.left = TreeNode(nodeList[3])
root.left.right = TreeNode(nodeList[4])
root.right.left = TreeNode(nodeList[5])
root.right.right = TreeNode(nodeList[6])
L = 7
R = 15
x.rangeSumBST(root,L,R)

nodeList = [10,5,15,3,7,13,18,1,0,6] #10
root = TreeNode(nodeList[0])
root.left = TreeNode(nodeList[1])
root.right = TreeNode(nodeList[2])
root.left.left = TreeNode(nodeList[3])
root.left.right = TreeNode(nodeList[4])
root.right.left = TreeNode(nodeList[5])
root.right.right = TreeNode(nodeList[6])
root.left.left.left = TreeNode(nodeList[7])
root.left.left.right = TreeNode(nodeList[8])
root.left.right.left = TreeNode(nodeList[9])
L = 7
R = 15
x.rangeSumBST(root, L, R)