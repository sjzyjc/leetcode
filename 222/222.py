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
        T: logN ^ logN
        """
        if not root:
            return 0
        
        left_edge = self.findLeft(root.left)
        right_edge = self.findRight(root.right)
        
        if left_edge == right_edge:
            return (1 << (left_edge + 1)) - 1 
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
    
    def findLeft(self, node):
        if not node:
            return 0
        
        return self.findLeft(node.left) + 1
    
    def findRight(self, node):
        if not node:
            return 0
        
        return self.findRight(node.right) + 1