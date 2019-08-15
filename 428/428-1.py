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
            return '#'
        
        ans = str(root.val)
        for child in root.children:
            ans += '|' + self.serialize(child)
            
        return ans + '|#'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        #print(data)
        if data == '#':
            return None
        
        queue = deque(data.split('|'))
        #print(queue)
        return self.helper(queue)
        
    def helper(self, queue):     
        val = int(queue.popleft())
        children = []
        while queue[0] != '#':
            child = self.helper(queue)
            children.append(child)
        
        queue.popleft()
        node = Node(val, children)
        
        return node
        
            
            
        
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))