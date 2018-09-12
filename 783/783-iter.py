# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.cur = None
        self.smallest = (1 << 31) - 1
        self.inOrder(root)
        return self.smallest
    
    def inOrder(self, node):
        if not node:
            return 
        
        self.inOrder(node.left)
        if self.cur is not None and abs(node.val - self.cur.val) < self.smallest:
            self.smallest = abs(node.val - self.cur.val)
            
        self.cur = node
        self.inOrder(node.right)
        
        
    
            
            
            