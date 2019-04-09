"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        queue = deque([root])
        prev = None
        while queue:
            level = len(queue)
            for _ in range(level):
                node = queue.popleft()
                    
                if prev:
                    prev.next = node
                    
                prev = node
                
                if not node: 
                    continue
                    
                queue.append(node.left)
                queue.append(node.right)
                
            prev = None
            
        return root
            