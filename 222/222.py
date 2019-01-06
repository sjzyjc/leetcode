# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        left_most_depth = self.leftDepth(root)
        right_most_depth = self.rightDepth(root)
        
        #perfect tree
        if left_most_depth == right_most_depth:
            return (1 << left_most_depth) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def leftDepth(self, node):
        if not node:
            return 0
        
        depth = 0
        while node:
            node = node.left
            depth += 1
        
        return depth
    
    def rightDepth(self, node):
        if not node:
            return 0
        
        depth = 0
        while node:
            node = node.right
            depth += 1
            
        return depth
            