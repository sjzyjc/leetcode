# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        
        return self.findPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def findPath(self, node, target):
        if not node:
            return 0
        
        count = 0
        if node.val == target:
            count += 1
            
        return count + self.findPath(node.left, target - node.val) + self.findPath(node.right, target - node.val)
            
        