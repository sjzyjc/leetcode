# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([root])
        ret = -1
        while queue:
            node = queue.popleft()
            if not node:
                continue

            ret = node.val
            queue.append(node.right)
            queue.append(node.left)
            
        return ret