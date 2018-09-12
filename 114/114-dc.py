# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
            
    def helper(self, root):
        if not root:
            return None
        
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        if right_last is None and left_last is None:
            return root
        
        if right_last is None:
            root.right = root.left
            root.left = None
            return left_last
             
        if left_last is None:    
            return right_last
        
        right = root.right
        root.right = root.left
        root.left = None
        left_last.right = right
        
        return right_last
            