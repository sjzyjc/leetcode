# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return  True
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second_init = slow
        prev = slow
        iterator = slow.next
        while iterator:
            nextt = iterator.next
            iterator.next = prev
            prev = iterator
            iterator = nextt
            
        first = head
        last = prev
        while first != second_init.next:
            if first.val != last.val:
                return False
            
            first = first.next
            last = last.next
            
        return True