# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if not head:
            return None
        
        node = head
        while node:
            new_node = RandomListNode(node.label)
            new_node.next = node.next
            node.next = new_node
            node = node.next.next
        
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
            
        node = head
        ans = head.next
        while node:
            clone_node = node.next
            next_node = node.next.next
            if next_node:
                clone_node.next = next_node.next
            
            node.next = next_node
            node = next_node
        
        return ans
        
        
        