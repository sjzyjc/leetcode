# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        stack = [root]
        while stack:
            node = stack[-1]
            if node is None:
                return None
            
            if node.val == p.val:
                break
            elif node.val < p.val:
                stack.append(node.right)
            else:
                stack.append(node.left)
                
        return self.findNext(stack)
        
    
    def findNext(self, stack):
        node = stack.pop()
        
        if node.right:
            node = node.right
            while node.left:
                node = node.left
                
            return node
        
        while stack and stack[-1].val < node.val:
            stack.pop()
            
        return stack[-1] if stack else None
        
        
                
            