# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        cur = ans
        merged = self.nodeToList(l1) + self.nodeToList(l2)
        merged.sort()
        if not merged:
            return None
        
        for i in range(len(merged)):
            cur.val = merged[i]
            
            if i != len(merged) - 1:
                cur.next = ListNode()
                cur = cur.next
        

        return ans
    
    def nodeToList(self, l: ListNode) -> list:
        tmp = []
        while(l != None):
            tmp.append(l.val)
            l = l.next
        
        return tmp