# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import *
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = []
        while head:
            node.append(head.val)
            head = head.next
            
        l = len(node)
        if l%2 == 0:
            # Even elements
            if not node:
                return True
            
            a = node[:int(l/2)]
            b = node[int(l/2):]
            b.reverse()
            
            return a == b
            
        else:
            # Odd elements
            
            a = node[:int(l//2)]
            b = node[int((l//2)+1):]
            b.reverse()
            
            return a == b