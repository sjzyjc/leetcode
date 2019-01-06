# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return self.helper(root, False)
    
    def helper(self, root, is_left):
        if not root:
            return 0
        
        if root.left is None and root.right is None and is_left:
            return root.val
        
        left_sum = self.helper(root.left, True)
        right_sum = self.helper(root.right, False)
        
        return left_sum + right_sum