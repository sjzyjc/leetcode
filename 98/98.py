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
        self.isValid = True
        self.cmpVal(root)
        return self.isValid
    
    def cmpVal(self, node):
        if not node:
            return
        
        left_is_BST = self.cmpVal(node.left)
        if self.prev != None and node.val <= self.prev:
            self.isValid = False 
        
        self.prev = node.val
        right_is_BST = self.cmpVal(node.right)
        
        
        