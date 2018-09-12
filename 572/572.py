# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        if t is None:
            return True
        
        if s is None:
            return False
        
        return self.equals(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def equals(self, s, t):
        if s is None and t is None:
            return True
        
        if (s is None) != (t is None):
            return False
        
        if s.val != t.val:
            return False
        
        return self.equals(s.left, t.left) and self.equals(s.right, t.right) 
        
        
        