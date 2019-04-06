
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        
        stack = [head]
        prev = None
        
        while stack:
            node = stack.pop()
            #print(node.val)
            
            if prev: prev.next = node
            node.prev = prev
            
            if node.next:
                stack.append(node.next)
                #node.next = None
                
            if node.child:
                stack.append(node.child)
                node.child = None
                
            prev = node
              
        return head
            
        
        