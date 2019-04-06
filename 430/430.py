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
        
        self.helper(head)
        return head
    
    def helper(self, node):
        #print(node.val)
        if not node:
            return None
        
        prev = None
        ptr = node 
        while ptr:
            if not ptr.child:
                prev = ptr
                ptr = ptr.next
                continue
                
            nextt = ptr.next
            child = ptr.child
            child_tail = self.helper(child)
                
            ptr.next = child
            child.prev = ptr
                
            child_tail.next = nextt
            if nextt:
                nextt.prev = child_tail
                
            ptr.child = None
            
            prev = child_tail
            ptr = nextt
            
        return prev
            
        
        