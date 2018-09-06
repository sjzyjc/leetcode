"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = deque([root])
        ret = []
        while queue:
            length = len(queue)
            ret.append([])
            
            for i in range(length):
                node = queue.popleft()
                
                ret[len(ret) - 1].append(node.val)
                for child in node.children:
                    queue.append(child)
                    
        return ret
                