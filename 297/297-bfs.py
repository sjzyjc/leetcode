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
        if root is None:
            return ['#']
        
        queue = deque([root])
        ans= []
        while queue:
            node = queue.popleft()
            if not node:
                ans += ['#']
            else:
                ans += [node.val]
                queue.append(node.left)
                queue.append(node.right)
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        root_val = data.pop(0)
        if root_val == '#':
            return None
        root = TreeNode(root_val)
        queue = deque([root])
        is_left = True
        
        while data:
            val = data.pop(0)
            
            node = TreeNode(val)
            if val == '#':
                node = None
                                
            if is_left:
                queue[0].left = node
            else:
                queue[0].right = node
                queue.popleft()
            
            is_left = not is_left
            if node is not None:
                queue.append(node)
        return root
            
            
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))