# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        result = []
        if N == 0:
            return result
        
        if N == 1:
            result.append(TreeNode(0))
        elif N == 2:
            pass
        elif N == 3:
            tmp = TreeNode(0)
            tmp.left = TreeNode(0)
            tmp.right = TreeNode(0)
            result.append(tmp)
        else:
            for i in range(1, N-1, 2):
                for j in self.allPossibleFBT(i):
                    for k in self.allPossibleFBT(N-i-1):
                        tmp = TreeNode(0)
                        tmp.left = j
                        tmp.right = k
                        result.append(tmp)
                
        return result