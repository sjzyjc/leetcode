# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max = 0
        self.find(root)
        return self.max
        
        
    
    def find(self, node):
        if not node:
            return 0, None, None, True
        
        left_size, min_left, max_left, is_left_BST = self.find(node.left)
        right_size, min_right, max_right, is_right_BST = self.find(node.right)
        
        if not is_left_BST or not is_right_BST:
            return None, None, None, False
        
        if max_left is not None and node.val <= max_left:
            return None, None, None, False
        
        if min_right is not None and node.val > min_right:
            return None, None, None, False
        
        
        max_val = node.val
        min_val = node.val
        if max_right is not None:
            max_val = max_right
            
        if min_left is not None:
            min_val = min_left
            
        self.max = max(self.max, left_size + right_size + 1)
        
        return left_size + right_size + 1, min_val, max_val, True
        