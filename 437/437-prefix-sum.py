# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        O(N)
        """
        if not root:
            return 0
        
        self.count = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        
        self.helper(root, prefix, 0, sum)
        return self.count
        
    def helper(self, node, prefix, carry, target):
        if node is None:
            return 
        
        carry += node.val
        if carry - target in prefix:
            self.count += prefix[carry - target]
            
        prefix[carry] += 1
        
        self.helper(node.left, prefix, carry, target)
        self.helper(node.right, prefix, carry, target)
        
        prefix[carry] -= 1
        
            
        
            
        