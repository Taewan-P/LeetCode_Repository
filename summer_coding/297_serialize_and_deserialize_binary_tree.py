# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json
from TreeNode import *
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # print(str(self.treeToList(root)))
        
        return str(self.treeToList(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # list_data = ast.literal_eval(data)
        list_data = json.loads(data)
        return self.deserialize_list(list_data)
            
        
    def deserialize_list(self, data):
        """
        Decodes List to treeNode
        """
        if data:
            result = TreeNode(data[0])
            
            for i, n in enumerate(data):
                if i == 0:
                    continue
                if type(n) == list:
                    if i == 1:
                        # Left
                        result.left = self.deserialize_list(n)
                    else:
                        # Right
                        result.right = self.deserialize_list(n)
                else:
                    if type(n) == int and n != 0:
                        if i == 1:
                            # Left
                            result.left = TreeNode(n)
                        else:
                            # Right
                            result.right = TreeNode(n)
            
            return result
                    
        else:
            return None


    def treeToList(self, tree):
        node = []
        if not tree:
            return []
        node.append(tree.val)
        
        if tree.left:
            node.append(self.treeToList(tree.left))
        else:
            node.append(0)

        if tree.right:
            node.append(self.treeToList(tree.right))
        else:
            node.append(0)
                
        return node
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))