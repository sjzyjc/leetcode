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
        if not root:
            return True
        
        max_val, min_val, is_BST = self.devideConquer(root)
        return is_BST

    def devideConquer(self, node):
        if not node:
            return None, None, True

        max_left, min_left, left_is_BST = self.devideConquer(node.left)
        max_right, min_right, right_is_BST = self.devideConquer(node.right)

        if not left_is_BST or not right_is_BST:
            return None, None, False

        if max_left is not None and not (node.val > max_left):
            return None, None, False

        if min_right is not None and not (node.val < min_right):
            return None, None, False

        max_val, min_val = node.val, node.val
        if max_right is not None:
            max_val = max_right

        if min_left is not None:
            min_val = min_left

        print(max_val, min_val)
        return max_val, min_val, True
        
        
        