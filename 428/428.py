"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root is None:
            return []
        
        queue = deque([root])
        ans = []
        ans.append(['#', root.val])
        
        while queue:
            node = queue.popleft()
            child_list = []
            for child in node.children:
                child_list.append(child.val)
                queue.append(child)
            ans.append([node.val, child_list])
        
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if len(data) == 0:
            return None

        root_val = data.pop(0)[1]
        root_node = Node(root_val, [])
        queue = deque([root_node])
        
        while queue:
            node = queue.popleft()
            
            for child in data.pop(0)[1]:
                child_node = Node(child, [])
                node.children.append(child_node)
                queue.append(child_node)
        
        return root_node
                
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))