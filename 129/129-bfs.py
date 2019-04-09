# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([(root, root.val)])
        
        ans = 0
        while queue:
            node, carry = queue.popleft()
                
            if not node.left and not node.right:
                ans += carry
                continue
            
            if node.left:
                queue.append((node.left, carry * 10 + node.left.val))
                
            if node.right:
                queue.append((node.right, carry * 10 + node.right.val))
                
        return ans
        
        
        