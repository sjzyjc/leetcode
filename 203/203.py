# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        dummy = ListNode('#')
        dummy.next = head
        iterator = head
        prev = dummy
        
        while iterator:
            if iterator.val == val:
                prev.next = iterator.next
                iterator = iterator.next
                continue
                
            prev = iterator
            iterator = iterator.next
            
        return dummy.next