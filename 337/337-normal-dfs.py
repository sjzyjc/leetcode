# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return max(self.dfs(root))
    
    def dfs(self, node):
        if not node:
            return 0, 0
        
        left_rob, left_no = self.dfs(node.left)
        right_rob, right_no = self.dfs(node.right)
        
        return node.val + left_no + right_no, max(left_rob, left_no) + max(right_rob, right_no)
        