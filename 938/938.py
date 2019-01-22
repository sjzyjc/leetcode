# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root or L > R:
            return 0
        
        node = root
        stack = []
        while node:
            if node.val == L:
                stack.append(node)
                break
            elif node.val > L:
                stack.append(node)
                node = node.left
            else:
                node = node.right
                
        ans = 0        
        while stack and  stack[-1].val <= R:
            node = stack.pop()
            ans += node.val
            
            node = node.right
            while node:
                stack.append(node)
                node = node.left
                
        return ans
                
        