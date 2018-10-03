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
        if not root:
            return []
        
        stack = []
        ret = []
        node = root
        
        while stack or node:
            if node:
                stack.append(node)
                ret.append(node.val)
                node = node.right
            else:
                node = stack.pop()
                node = node.left   
        return ret[::-1]