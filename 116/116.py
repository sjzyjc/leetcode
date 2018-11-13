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
        self.dfs(node.left, node.right)
        self.dfs(node.right, node.next.left if node.next else None)
        
        
        
        