# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # write your code here
        if root is None:
            return "()"
        
        return "(" + str(root.val) + self.serialize(root.left) + self.serialize(root.right) + ")"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #print(data)
        if not data:
            return None
        
        data = deque(list(data))
        return self.dfs(data)
        
    def dfs(self, data):
        if not data or data[0] == ')':
            return None
        
        if data[0] == '(':
            data.popleft()
            
        if data[0] == ')':
            data.popleft()
            return None
        
        next_char = ""
        while data and (data[0] != '(' and data[0]!=')'):
            next_char += data.popleft()
        
        #print(next_char)
        cur = TreeNode(next_char)
        cur.left = self.dfs(data)
        cur.right = self.dfs(data)
            
        #print(cur.val, data)
        data.popleft()
        return cur
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))