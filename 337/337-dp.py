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
        
        memo = {}
        return self.dfs(root, memo)
    
    def dfs(self, node, memo):
        if not node:
            return 0
        
        if node in memo:
            return memo[node]
        
        rob_score = node.val
        if node.left:
            rob_score += self.dfs(node.left.left, memo)
            rob_score += self.dfs(node.left.right, memo)
            
        if node.right:
            rob_score += self.dfs(node.right.left, memo)
            rob_score += self.dfs(node.right.right, memo)
            
        no_rob = self.dfs(node.left, memo) + self.dfs(node.right, memo)
        memo[node] = max(rob_score, no_rob)
        
        return memo[node]
        