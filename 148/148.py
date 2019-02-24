# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        if head.next is None:
            return head
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        next_head = slow.next
        slow.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(next_head)
        return self.merge(head1, head2)
    
    def merge(self, head1, head2):
        if head1 is None:
            return head2
        
        if head2 is None:
            return head1
        
        head = None
        prev = None
        if head1.val < head2.val:
            head = prev = head1
            head1 = head1.next
        else:
            head = prev = head2
            head2 = head2.next
        
        while head1 and head2:
            if head1.val < head2.val:
                prev.next = head1
                prev = head1
                head1 = head1.next
            
            else:
                prev.next = head2
                prev = head2
                head2 = head2.next
        
        if head2:
            prev.next = head2
        
        if head1:
            prev.next = head1
            
        return head
        