"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        
        cloned = {}
        return self.helper(node, cloned)
    
    def helper(self, node, cloned):
        if node in cloned:
            return cloned[node]
        
        new_node = Node(node.val, [])
        cloned[node] = new_node
        for nei in node.neighbors:
            new_node.neighbors.append(self.helper(nei, cloned))
            
        return new_node
        