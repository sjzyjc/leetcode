# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack = [(root, 0)]
        ret = []
        while stack:
            node, level = stack.pop()
            
            if not node:
                continue

            if level > len(ret) - 1:
                ret.insert(0, [])
            ret[-(level + 1)].append(node.val)        
            
            stack.append(node.right, level + 1)
            stack.append(node.left, level + 1)

        return ret
        