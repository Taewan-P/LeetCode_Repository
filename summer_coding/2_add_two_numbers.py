# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.getStrNum(l1)
        num2 = self.getStrNum(l2)
        
        sol = int(num1) + int(num2)
        

        tmp = list(str(sol))
        tmp.reverse()
        print(tmp)
        
        for i in range(len(tmp)):
            if i == 0:
                ans = ListNode(tmp[0])
                a = ans
            else:
                a.next = ListNode(tmp[i])
                a = a.next
            # print(ans)
                
        # for i in tmp:
        #     a.next = ListNode(i)
        #     a = ans.next
            
            
        return ans
        
        
    def getStrNum(self, l: ListNode) -> str:
        tmp = ""
        while (l != None):
            tmp = str(l.val) + tmp
            l = l.next
            
        return tmp
        
    
            
        