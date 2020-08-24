# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import *
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b = []
        while head:
            b.append(head.val)
            head = head.next
            
        return int("".join([str(i) for i in b]), 2)