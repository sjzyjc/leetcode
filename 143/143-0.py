# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        slow, fast = head, head.next
        
        #find mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        it = slow.next
        slow.next = None
        #reverse 2nd half
        while it:
            next_it = it.next
            it.next = prev
            
            prev = it
            it = next_it
            
        right = prev
        left = head
        
        while left and right:
            next_left = left.next
            left.next = right
            
            next_right = right.next
            right.next = next_left
            
            left = next_left
            right = next_right
            
                        
        