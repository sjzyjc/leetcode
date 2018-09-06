# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        self.dfs(root)
        return self.ret
    
    def dfs(self, node):
        if not node:
            return 
        
        self.dfs(node.left)
        self.dfs(node.right)

        self.ret.append(node.val)