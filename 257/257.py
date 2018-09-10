# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        if root.left is None and root.right is None:
            return [str(root.val)]
        
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
        
        ans = []
        for left_path in left_paths:
            ans.append(str(root.val) + "->" + left_path)
        
        for right_path in right_paths:
            ans.append(str(root.val) + "->" + right_path)
            
        return ans
        