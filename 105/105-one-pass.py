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
        
        j = 0
        root = TreeNode(preorder[0])
        stack = [root]
        
        for i in preorder[1:]:
            parent = stack[-1]
            is_left = True
            node = TreeNode(i)
            
            while stack and inorder[j] == stack[-1].val:
                parent = stack.pop()
                is_left = False
                j += 1
                
            if is_left:
                parent.left = node
            else:
                parent.right = node
            
            stack.append(node)
            
        return root
                
            
                
                
            
                
            