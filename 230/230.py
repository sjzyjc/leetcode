# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.counter = 0
        self.kth = None
        self.inOrder(root, k)
        return self.kth
        
    def inOrder(self, node, k):
        if not node:
            return
        
        self.inOrder(node.left, k)
        self.counter += 1
        if self.counter == k:
            self.kth = node.val
        if self.counter < k:
            self.inOrder(node.right, k)