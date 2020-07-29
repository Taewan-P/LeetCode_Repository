# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        if root:
            result.append(root.val)
        else:
            return []
        
        if root.left:
            result += self.preorderTraversal(root.left)
        
        if root.right:
            result += self.preorderTraversal(root.right)
            
        return result