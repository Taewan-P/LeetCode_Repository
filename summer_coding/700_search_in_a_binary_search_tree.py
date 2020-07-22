# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        elif root.val == val:
            return root
        elif root.val > val:
            # Value is smaller
            return self.searchBST(root.left, val)
        elif root.val < val:
            # Value is bigger
            return self.searchBST(root.right, val)