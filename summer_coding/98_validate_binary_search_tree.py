# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        ans = False
        if root.left:
             ans = root.val > self.maxValue(root.left)
        else:
            ans = True
                
        if root.right:
            ans = ans and (root.val < self.minValue(root.right))
        else:
            ans = ans and True
        
        if ans:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False
                  
            
    def maxValue(self, root: TreeNode) -> int:
        return 0 if not root else max(self.preorderTraversal(root))
            
    def minValue(self, root: TreeNode) -> int:
        return 999 if not root else min(self.preorderTraversal(root))
        
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