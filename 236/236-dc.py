# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return -1
        
        self.ans = None
        self.helper(root, p, q)
        return self.ans
    
    
    def helper(self, node, p, q):
        if not node:
            return False, False
        
        l_found_p, l_found_q = self.helper(node.left, p, q)
        r_found_p, r_found_q = self.helper(node.right, p, q)
        
        #if p, q not each other's ancester
        if (l_found_p and r_found_q) or (l_found_q and r_found_p):
            self.ans = node
        
        found_p = l_found_p or r_found_p
        found_q = l_found_q or r_found_q
        if node == p:
            found_p = True
            if l_found_q or r_found_q:
                self.ans = p
            
        if node == q:
            found_q = True
            if l_found_p or r_found_p:
                self.ans = q
        
        return found_p, found_q