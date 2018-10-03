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
        if frequent call kth smallest, we could cache left size for each node
        T： h instead of k + h

        """
        
        node = root
        while node is not None:
            left_size = self.findSize(node.left)
            
            if left_size + 1 == k:
                return node.val
            elif left_size + 1 < k:
                node = node.right
                k -= (left_size + 1)
            else:
                node = node.left
                
        return None
    
    def findSize(self, node):
        if not node:
            return 0
        
        left_size = self.findSize(node.left)
        right_size = self.findSize(node.right)
        
        return left_size + right_size + 1