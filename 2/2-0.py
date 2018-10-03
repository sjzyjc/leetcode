 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if not l1 and not l2:
            return ListNode(0)
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        l1_node = l1
        l2_node = l2
        carry = 0
        l1_prev = None
                
        while l1_node or l2_node or carry == 1:
            if l2_node and not l1_node:
                l1_node = ListNode(0)
                l1_prev.next = l1_node
            
            if l1_node and not l2_node:
                l2_node = ListNode(0)
                
            if not l1_node and not l2_node and carry == 1:
                l1_node = ListNode(0)
                l2_node = ListNode(0)
                l1_prev.next = l1_node
                
            pos_sum = l1_node.val + l2_node.val + carry
            
            if pos_sum > 9:
                carry = 1
            else:
                carry = 0
            
            l1_node.val = pos_sum % 10 

            l1_prev = l1_node
            l1_node = l1_node.next
            l2_node = l2_node.next
        
        return l1
    