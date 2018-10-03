# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 0:
            return head
        
        count = 1
        iterator = head
        while iterator.next:
            iterator = iterator.next
            count += 1
        
        if k % count == 0:
            return head
        
        k = count - (k % count) - 1
        tail = head
        while k > 0:
            tail = tail.next
            k -= 1
        
        ans = tail.next
        tail.next = None
        iterator.next = head
        
        return ans