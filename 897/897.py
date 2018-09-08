# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.cur = TreeNode(None)
        ans = self.cur
        self.inOrder(root)
        return ans.right
    
    def inOrder(self, node):
        if not node:
            return
        
        self.inOrder(node.left)
        node.left = None
        self.cur.right = node
        self.cur = node
        self.inOrder(node.right)
        
        