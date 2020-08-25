class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = [root]
        depth = 0
        
        if not root:
            return depth
        
        while queue:
            l = len(queue)
            for i in range(l):
                queue += queue[0].children
                queue.pop(0)
            
            depth += 1

        return depth