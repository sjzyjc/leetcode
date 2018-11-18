# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        
        dummy = ListNode("#")
        dummy.next = head
        
        node1 = head
        prev = dummy
        while node1 and node1.next:
            node2 = node1.next
            next = node2.next
                
            prev.next = node2
            node2.next = node1
            node1.next = next
                
            prev = node1
            node1 = node1.next
            
        return dummy.next
                
                
            