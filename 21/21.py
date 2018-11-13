# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        h1 = l1
        h2 = l2
        dummy = ListNode("#")
        prev = dummy
        while l1 or l2:   
            node = None

            if not l1:
                node = l2
                l2 = l2.next
            
            elif not l2:
                node = l1
                l1 = l1.next
                
            elif l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
                
            prev.next = node
            prev = node
            
        return dummy.next
                
                