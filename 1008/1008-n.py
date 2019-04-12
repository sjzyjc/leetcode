# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def bstFromPreorder(self, pre: List[int]) -> TreeNode:
        if not pre:
            return None
        
        pre = deque(pre)
        return self.preorder(pre, -(1 << 31), (1 << 31) - 1)
    
    def preorder(self, pre, low_bound, upper_bound):
        if not pre or not (low_bound <= pre[0] <= upper_bound):
            return None
        
        node = TreeNode(pre.popleft())
        node.left = self.preorder(pre, low_bound, node.val - 1)
        node.right = self.preorder(pre, node.val + 1, upper_bound)
        
        return node
        
        
        