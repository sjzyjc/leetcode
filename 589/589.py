"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = list([root])
        ret = []
        while stack:
            node = stack.pop()
            ret.append(node.val)
            
            for i in range(len(node.children)):
                stack.append(node.children[len(node.children) - 1 - i])
                
        return ret