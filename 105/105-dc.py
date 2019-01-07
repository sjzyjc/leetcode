# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        node = TreeNode(preorder[0])
        j = 0
        while inorder[j] != node.val:
            j += 1
            
        node.left = self.buildTree(preorder[1: j + 1], inorder[:j])
        node.right = self.buildTree(preorder[j+1: ], inorder[j+1:])
        return node