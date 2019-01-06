# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.cmpVal(root)
    
    def cmpVal(self, node):
        if not node:
            return True
        
        left_is_BST = self.cmpVal(node.left)
        if left_is_BST is False:
            return False
        
        if self.prev != None and node.val <= self.prev:
            return False 
        
        self.prev = node.val
        return self.cmpVal(node.right)
        
        
        
        