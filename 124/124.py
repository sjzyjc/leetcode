# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return False
        
        self.ans = -(1 << 31)
        self.dfs(root)
        return self.ans
    
    def dfs(self, node):
        if not node:
            return 0
        
        left_path = self.dfs(node.left)
        right_path = self.dfs(node.right)
        
        cur_sum = node.val
        cur_path = node.val
        if left_path > 0:
            cur_sum += left_path
            cur_path += left_path
            
        if right_path > 0:
            cur_sum += right_path
            cur_path = max(cur_path, node.val + right_path)
            
        #update ans
        self.ans = max(self.ans, cur_sum)
        return cur_path