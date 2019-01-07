# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        return self.helper(inorder, postorder)
    
    def helper(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        node = TreeNode(postorder[-1])
        
        index = 0
        while inorder[index] != node.val:
            index += 1
            
        node.left = self.helper(inorder[:index], postorder[:index])
        node.right = self.helper(inorder[index + 1:], postorder[index:len(postorder) - 1])
        
        return node
            