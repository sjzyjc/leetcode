# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        left_tree = self.pruneTree(root.left)
        right_tree = self.pruneTree(root.right)
        
        root.left = left_tree
        root.right = right_tree
        
        if left_tree is None and right_tree is None and root.val == 0:
            return None
        
        return root