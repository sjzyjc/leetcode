# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        
        self.dfs(root, None)
        
    def dfs(self, node, other):
        if not node:
            return
        
        node.next = other
        
        next = None
        iterator = node.next
        while iterator:
            if iterator.left:
                next = iterator.left
                break
            if iterator.right:
                next = iterator.right
                break
                
            iterator = iterator.next
    
        if node.right:
            self.dfs(node.right, next)
            self.dfs(node.left, node.right)

        else:
            self.dfs(node.left, next)
                
    