# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
            
        if not s:
            return False
        
        return self.hash(t) in self.hash(s)
    
    def hash(self, node):
        if not node:
            return '#'
        
        return '|' + str(node.val) +'|'+ self.hash(node.left) + self.hash(node.right)
            
            
        
            
        
        
        