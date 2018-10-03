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

        queue = deque([(root, 1)])
        level = - (1 << 31)
        while queue:
            node, level = queue.popleft()

            if not node:
                continue
            
            for child in node.children:
                queue.append((child, level + 1))
        
        return level
