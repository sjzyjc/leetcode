# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:   
            return False
        
        slow, fast = head, head
        while fast:
            slow = slow.next
            
            if fast.next is None:
                break
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False