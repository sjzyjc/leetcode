# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
    
        return self.dfs(root, 0)[1]
    
    
    def dfs(self, node, depth):
        if not node:
            return depth, None
        
        left_deepest, left_ans = self.dfs(node.left, depth + 1)
        right_deepest, right_ans = self.dfs(node.right, depth + 1)
        
        if left_deepest > right_deepest:
            return left_deepest, left_ans
        elif right_deepest > left_deepest:
            return right_deepest, right_ans
        else:
            return left_deepest, node
            
        
        