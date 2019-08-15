# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        self.dfs(root, sum, ans, [])
        return ans
    
    def dfs(self, node, target, ans, carry):
        if not node:
            return 
        
        carry.append(node.val)
        if node.val == target and not node.left and not node.right:
            ans.append(carry + [])
            carry.pop()
            return    
        
        self.dfs(node.left, target - node.val, ans, carry)
        self.dfs(node.right, target - node.val, ans, carry)
        carry.pop()
        