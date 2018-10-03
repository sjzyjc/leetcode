# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        
        orig = root
        while root:
            if root.val < val:
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                root = root.right
            else:
                if root.left is None:
                    root.left = TreeNode(val)
                    break
                root = root.left

        
        return orig
        
        