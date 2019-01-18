"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        dummy = Node('#', None, None)
        
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
            
        dummy.right = stack[-1]
        while stack:
            cur = stack.pop()
            
            node = cur.right
            while node:
                stack.append(node)
                node = node.left
            
            if stack:
                cur.right = stack[-1]
                stack[-1].left = cur
            
            
        cur.right = dummy.right
        dummy.right.left = cur
        
        return dummy.right
            
        
        
            
        
        