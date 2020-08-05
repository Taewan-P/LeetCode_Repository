# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import *
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        l = []
        if not head:
            return None
        
        while head:
            l.append(head.val)
            head = head.next
            
        l.sort()
        
        result = ListNode()
        cur = result
        for i, n in enumerate(l):
            if i == 0:
                result = ListNode(n)
                cur = result
            else:
                cur.next = ListNode(n)
                cur = cur.next

        return result