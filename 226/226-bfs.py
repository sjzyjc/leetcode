# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                continue
                
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
            
        return root