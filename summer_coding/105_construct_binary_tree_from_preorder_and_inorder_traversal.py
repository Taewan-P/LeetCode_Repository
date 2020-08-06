# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        ri = inorder.index(preorder[0]) # Root Index
        
        left_inorder = inorder[:ri]
        right_inorder = inorder[ri+1:]
        
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        
        tree = TreeNode(preorder[0])
        if len(left_inorder) == 1:
            tree.left = TreeNode(left_inorder[0])
        else:
            tree.left = self.buildTree(left_preorder, left_inorder)
            
        if len(right_inorder) == 1:
            tree.right = TreeNode(right_inorder[0])
        else:
            tree.right = self.buildTree(right_preorder, right_inorder)
        
        return tree