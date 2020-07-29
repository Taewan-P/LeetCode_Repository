# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        s = S.split("-") # s = ['1', '2', '', '3', '', '4', '5', '', '6', '', '7']
        result = TreeNode(s[0])
        s = s[1:]
        left = []
        right = []
        
        state = False
        for i, j in enumerate(s):
            if j.isdigit():
                if state:
                    # Another branch
                    left = s[:i]
                    right = s[i:]
                    break
                else:
                    state = True
            else:
                state = False
                
        if (not left and not right) and s:
            left = s
                    
        # left = ['2', '', '3', '', '4']    
        # right = ['5', '', '6', '', '7']
        
        left = ["-" if i == "" else i for i in left]
        right = ["-" if i == "" else i for i in right]
        
        left_s = "".join(left)
        right_s = "".join(right)
        
        # left_s = "2-3-4"
        # right_s = "5-6-7"
        
        if left_s != "":
            result.left = self.recoverFromPreorder(left_s)
        if right_s != "":
            result.right = self.recoverFromPreorder(right_s)
        
        return result