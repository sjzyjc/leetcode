# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = deque()
        queue.append((root, 0))
        ret = []

        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            
            if level > len(ret) - 1:
                ret.append([])
            
            ret[level].append(node.val)

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return ret    