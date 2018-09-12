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
        
        max_val, min_val, min_diff = self.helper(root)
        return min_diff
    
    def helper(self, root):
        if not root:
            return None, None, (1 << 31) - 1
        
        left_max, left_min, left_min_diff = self.helper(root.left)
        right_max, right_min, right_min_diff = self.helper(root.right)
        
        min_val = root.val
        max_val = root.val
        min_diff = min(left_min_diff, right_min_diff)
        if left_min is not None:
            min_val = left_min
        if right_max is not None:
            max_val = right_max
            
        if right_min is not None:
            min_diff = min(abs(root.val - right_min), min_diff)
            
        if left_max is not None:
            min_diff = min(abs(root.val - left_max), min_diff)
            
        return max_val, min_val, min_diff            