/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Solution {
    public ListNode middleNode(ListNode head) {
        int length = 1;
        ListNode c = head;
    
        while(true) {
            if(c.next == null){
                // length calc complete.
                break;
            }
            else {
                c = c.next;
                length++;
            }
        }
        
        for(int i = 0; i < length/2; i++){
            head = head.next;
        }
        return head;
        
    }
}