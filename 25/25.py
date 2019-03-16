# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k <= 1:
            return head
        
        dummy = prev_tail = ListNode('#')
        dummy.next = head
        prev = dummy
        node = head
        count = 0
        
        tail = None
        while node:
            count += 1
            
            nextt = node.next
            #reverse edge
            node.next = prev
            
            if count == 1: #tail node
                tail = node
                tail.next = None
                
            elif count == k: #head node
                prev_tail.next = node
                count = 0
                prev_tail = tail
                
            prev = node
            node = nextt
            
        if count != 0:
            tmp_prev = None
            tmp_cur = prev
            while tmp_prev != tail:
                nextt = tmp_cur.next
                tmp_cur.next = tmp_prev
                
                tmp_prev = tmp_cur
                tmp_cur = nextt
                
            prev_tail.next = tail
            
        
        return dummy.next
                
            
            
        