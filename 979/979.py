# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return self.helper(root)[0]
    
    def helper(self, node):
        #return no_moves, no_nodes - no_coins
        if not node:
            return 0, 0
        
        left_moves, left_diff = self.helper(node.left)
        right_moves, right_diff = self.helper(node.right)
        
        total_diff = left_diff + right_diff + 1 - node.val    
        return left_moves + right_moves + abs(total_diff), total_diff