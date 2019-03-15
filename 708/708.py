"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal, None)
        if not head:
            return new_node
        
        ret = head
        ptr = head.next
        insert = None
        not_done = True
        
        while not_done:
            #inbetween
            if ptr.val <= insertVal and ptr.next.val > insertVal:
                break
                
            #insert to the end
            if ptr.val <= insertVal and ptr.next.val < ptr.val:
                break
                
            #insert to the front
            if ptr.next.val > insertVal and ptr.next.val < ptr.val:
                break
                
            ptr = ptr.next
            if ptr == ret.next:
                not_done = False
               
        if not insert:
            insert = ptr
            
        #print(insert.val)    
        nextt = insert.next
        insert.next = new_node
        new_node.next = nextt
        
        return ret
        
            
        