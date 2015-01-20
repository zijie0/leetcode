# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        while root:
            new_sum = sum - root.val
            if new_sum == 0 and not root.left and not root.right:
                return True
            return self.hasPathSum(root.left, new_sum) or self.hasPathSum(root.right, new_sum)
        return False

root = TreeNode(5)
n1 = TreeNode(4)
n2 = TreeNode(8)
n3 = TreeNode(11)
n4 = TreeNode(13)
n5 = TreeNode(4)
n6 = TreeNode(7)
n7 = TreeNode(2)
n8 = TreeNode(1)
root.left = n1
root.right = n2
n1.left = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.right = n8

print Solution().hasPathSum(root, 22)