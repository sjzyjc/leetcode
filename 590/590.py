"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            
            ret.append(node.val)
            for child in node.children:
                stack.append(child)
        
        return ret[::-1]
            