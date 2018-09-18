# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            
            if root.right is None:
                return root.left
            
            node = root.right
            min_val = node.val
            while node.left:
                node = node.left
                min_val = node.val
            
            root.val = min_val
            root.right = self.deleteNode(root.right, min_val)
        
        return root