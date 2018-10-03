# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        return self.helper(root, p, q)[2]
        
    
    def helper(self, root, p, q):
        if not root:
            return False, False, None
        
        left_has_p, left_has_q, left_lca = self.helper(root.left, p, q)
        right_has_p, right_has_q, right_lca = self.helper(root.right, p, q)
        
        if left_lca:
            return True, True, left_lca
        
        if right_lca:
            return True, True, right_lca
        
        has_p = left_has_p or right_has_p or (root == p)
        has_q = left_has_q or right_has_q or (root == q)
        
        if (left_has_p and right_has_q) or (left_has_q and right_has_p) or (root == p and has_q) or (root == q and has_p):
            return True, True, root
        
        return has_p, has_q, None
        
        
        
        