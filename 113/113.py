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
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans = []
        self.helper(root, sum, ans, [])
        return ans
    
    
    def helper(self, node, target, ans, carry):
        if not node:
            return 
        
        carry.append(node.val)
        if node.left is None and node.right is None and node.val == target:
            ans.append(carry + [])
            
        self.helper(node.left, target - node.val, ans, carry)
        self.helper(node.right, target - node.val, ans, carry)
        carry.pop()
        
        return 
        
        