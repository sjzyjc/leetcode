# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root, v):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return [None, None]
        
        self.root = root
        node = root
        small_equal = first_small = TreeNode(-(1 << 31))
        large = first_large = TreeNode((1 << 31) - 1)
        
        small_equal.right = root
        large.left = root
        
        while node:
            if node.val == v:
                small_equal.right = node
                
                large.left = node.right
                node.right = None
                
                small_equal = node
                large = node.right
                break
                
            elif node.val < v:
                small_equal.right = node
                
                small_equal = node
                node = node.right
            else:
                large.left = node
                    
                large = node
                node = node.left
        
        if small_equal == first_small and large != first_large:
            return [None, first_large.left]
        
        if small_equal != first_small and large == first_large:
            return [first_small.right, None]
        
        if small_equal.val != v:
            large.left = None
            small_equal.right = None
        
        return [first_small.right, first_large.left]
        
            
                