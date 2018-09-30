# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.ans = 0
        self.helper(root, 0)
        return self.ans
    
    
    def helper(self, node, level):
        if not node:
            return 0
        
        left_depth = self.helper(node.left, level - 1)
        right_depth = self.helper(node.right, level - 1)
        
        self.ans = max(self.ans, left_depth + right_depth)
        
        return max(left_depth, right_depth) + 1