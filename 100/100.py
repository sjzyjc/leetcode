# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p is None) != (q is None):
            return False
        
        if p is None and q is None:
            return True
        
        left_same = self.isSameTree(p.left, q.left)
        right_same =  self.isSameTree(p.right, q.right)
        
        if not left_same or not right_same:
            return False
        
        if p.val != q.val:
            return False
        
        return True