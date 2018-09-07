# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        
        left, right = head, head.next
        while right is not None:
            if left.val == right.val:
                left.next = right.next
            else:
                left = right
            
            right = right.next
        
        return head

                