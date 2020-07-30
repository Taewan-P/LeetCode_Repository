# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        flipped = self.flipTree(root.right)
        return self.isIdentical(root.left, flipped)
            
            
    def flipTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        result = TreeNode(root.val)
        result.right = self.flipTree(root.left)
        result.left = self.flipTree(root.right)
        return result
    
    def isIdentical(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not (t1 or t2):
            return True if t1 == t2 else False
        else:
            if (t1 and t2) and (t1.val == t2.val):
                return self.isIdentical(t1.left, t2.left) and self.isIdentical(t1.right, t2.right)