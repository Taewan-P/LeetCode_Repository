# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import *
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        
        cur = head
        while cur:
            if cur.val == val:
                # When the first value of ListNode is equal to the element that we're trying to remove
                head = head.next
            else:
                if cur.next:
                    # If next node is available
                    if cur.next.val == val:
                        # If next value is the element
                        if cur.next.next:
                            # If next next value is available, link current node with next next node.
                            cur.next = cur.next.next
                            continue
                        else:
                            # There is no next value, so cut linked list.
                            cur.next = None
                else:
                    # The only and last element in the linked list
                    if cur.val == val:
                        return None
            
            cur = cur.next
            
        
                
        return head