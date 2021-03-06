# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        
        return max(left_max, right_max) + 1