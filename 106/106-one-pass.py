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
        
        root = TreeNode(postorder[-1])
        stack = [root]
        
        j = len(inorder) - 1
        for i in range(len(postorder) - 2, -1, -1):
            node = TreeNode(postorder[i])
            prev = stack[-1]
            is_right = True
            
            while stack and inorder[j] == stack[-1].val:
                prev = stack.pop()
                is_right =  False
                j -= 1
                
            if is_right:
                prev.right = node
            else:
                prev.left = node
                
            stack.append(node)
            
        return root
                