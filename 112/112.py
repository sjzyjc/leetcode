# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
            
        if root.left is None and root.right is None and root.val == target:
            return True
        
        return self.hasPathSum(root.left, target - root.val) or self.hasPathSum(root.right, target - root.val)
        
        