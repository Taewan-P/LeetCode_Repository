# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import *
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        tmp = []
        while cur != None:
            tmp.append(cur.val)
            cur = cur.next
            
        tmp.reverse()

        for i in range(len(tmp)):
            if i == 0:
                ans = ListNode(tmp[i])
                cur = ans
            else:
                cur.next = ListNode(tmp[i])
                cur = cur.next

        if tmp:
            return ans