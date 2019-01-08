# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return self.helper(root)[0]
    
    def helper(self, node):
        if not node:
            return 0, True
        
        left_count, left_is_uni = self.helper(node.left)
        right_count, right_is_uni = self.helper(node.right)
        
        if (not left_is_uni) or (not right_is_uni):
            return left_count + right_count, False
        
        left_val = node.left.val if node.left else None
        right_val = node.right.val if node.right else None
        
        if (left_val and left_val != node.val) or (right_val and right_val != node.val):
            return left_count + right_count, False
        
        return left_count + right_count + 1, True
        
            