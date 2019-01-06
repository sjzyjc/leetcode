# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = []
        while root:
            stack.append(root)
            root = root.left
            
        ans = []
        while stack:            
            node = stack.pop()
            ans.append(node.val)
            
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
                    
        return ans