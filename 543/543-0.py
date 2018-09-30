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
        
        return self.helper(root, 0)[1]
    
    
    def helper(self, node, level):
        if not node:
            return level - 1, 0
        
        left_depth, left_longest = self.helper(node.left, level + 1)
        right_depth, right_longest = self.helper(node.right, level + 1)
        
        maxium_depth = max(left_depth, right_depth, level)
        longest_path = max(left_depth + right_depth - 2 * level, left_longest, right_longest)
        
        return maxium_depth, longest_path