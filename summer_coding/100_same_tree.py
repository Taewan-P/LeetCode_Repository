# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.treeToList(p) == self.treeToList(q)
        
        
    def treeToList(self, tree: TreeNode) -> List[int]:
        node = []
        if not tree:
            return []
        node.append(tree.val)
        
        if tree.left:
            node.append(self.treeToList(tree.left))
        else:
            node.append(None)

        if tree.right:
            node.append(self.treeToList(tree.right))
        else:
            node.append(None)
                
        return node