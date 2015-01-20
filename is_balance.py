# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, root, depth):
        if not root:
            return True, 0
        ld, rd = 0, 0
        leftBalanced, new_ld = self.helper(root.left, ld)
        rightBalanced, new_rd = self.helper(root.right, rd)
        depth = 1 + max(new_ld, new_rd)
        return abs(new_ld - new_rd) < 2 and leftBalanced and rightBalanced, depth
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        depth = 0
        return self.helper(root, depth)[0]

root = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
root.left = n1
root.right = n2

print Solution().isBalanced(root)