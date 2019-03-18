# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.ans = 0
        self.dfs(root, 0)
        return self.ans
    
    #cur longest sigle path, current max
    def dfs(self, node, ans):
        if not node:
            return 0
        
        left_node = self.dfs(node.left, ans)    
        right_node = self.dfs(node.right, ans)
            
        cur_total = 1
        cur_node = 1
        if node.left and node.left.val == node.val:
            cur_total += left_node
            cur_node = left_node + 1
            
        if node.right and node.right.val == node.val:
            cur_total += right_node
            cur_node = max(cur_node, right_node + 1) 
               
        self.ans = max(self.ans, cur_total - 1)
        return cur_node
        
        
        