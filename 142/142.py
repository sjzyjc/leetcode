# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        node = head
        node_set = set()
        
        while node is not None:
            if node not in node_set:
                node_set.add(node)
            else:
                return node
            
            node = node.next
            
        return None
        