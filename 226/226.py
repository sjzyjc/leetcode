# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        self.helper(root)
        return root
    
    def helper(self, node):
        if not node:
            return
        
        self.helper(node.left)
        self.helper(node.right)
        
        node.left, node.right = node.right, node.left
        
        