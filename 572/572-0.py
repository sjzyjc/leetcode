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
        
        node_list = self.findRoot(s, t.val, [])
        for node in node_list:
            if self.validate(node, t):
                return True
        return False
    
    def findRoot(self, s, target, node_list):
        if not s:
            return node_list
        
        if s.val == target:
            node_list.append(s)
        
        self.findRoot(s.left, target, node_list)
        self.findRoot(s.right, target, node_list)
        
        return node_list
        
        
    def validate(self, s, t):
        if s is None and t is None:
            return True
        
        if (s is None) != (t is None):
            return False
        
        if s.val != t.val:
            return False
        
        left_is_sub = self.validate(s.left, t.left)
        right_is_sub = self.validate(s.right, t.right)
        
        return left_is_sub and right_is_sub
        
        