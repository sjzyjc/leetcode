# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        return self.computeTilt(root)[1]
    
    def computeTilt(self, node):
        if node is None:
            return 0, 0
        
        left_sum, left_tilt = self.computeTilt(node.left)
        right_sum, right_tilt = self.computeTilt(node.right)
        
        return left_sum + right_sum + node.val, abs(left_sum - right_sum) + left_tilt + right_tilt 
        