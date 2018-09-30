# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if not l1 and not l2:
            return None
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        stack1, stack2 = [], []
        it1, it2 = l1, l2
        while it1:
            stack1.append(it1.val)
            it1 = it1.next
        
        while it2:
            stack2.append(it2.val)
            it2 = it2.next
            
        carry = 0
        prev = None
        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
                
            if stack2:
                carry += stack2.pop()
            
            node = ListNode(carry % 10)
            node.next = prev
            prev = node
            carry = carry // 10
        
        return node