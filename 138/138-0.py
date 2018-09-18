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
        
        nodes = {}
        node = head
        while node:
            nodes[node] = RandomListNode(node.label)
            node = node.next
        
        for orig_node in nodes:
            if orig_node.next:
                nodes[orig_node].next = nodes[orig_node.next]
            if orig_node.random:
                nodes[orig_node].random = nodes[orig_node.random]
        
        return nodes[head]
            