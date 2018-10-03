"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        queue = deque([root])
        level = 0
        while queue:
            length = len(queue)
            level += 1
            for i in range(length):
                node = queue.popleft()
            
                for child in node.children:
                    queue.append(child)
            
        
        return level
