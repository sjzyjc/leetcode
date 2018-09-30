# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        reverse = False
        while queue:
            size = len(queue)
            level = []
             
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if not reverse:
                ans.append(level)
            else:
                ans.append(level[::-1])
                
            reverse = not reverse
        return ans
                