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
        
        return self.dfs(root, 0)
    
    #cur longest sigle path, current max
    def dfs(self, node, ans):
        if not node:
            return 0, ans
        
        left_long, left_ans = self.dfs(node.left, ans)    
        right_long, right_ans = self.dfs(node.right, ans)
            
        cur_ans = cur_long = 1
        if node.left and node.left.val == node.val:
            cur_ans += left_long
            cur_long += left_long
            
        if node.right and node.right.val == node.val:
            cur_ans += right_long
            cur_long = max(cur_long, right_long + 1)
               
        return cur_long, max(cur_ans, left_ans, right_ans)
        
        
        