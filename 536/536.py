# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
        
        s = deque("(" + s + ")")
        return self.helper(s)
    
    def helper(self, s):
        if not s:
            return None
        
        if s and s[0] == ")":
            return None
        
        if s[0] == '(':
            s.popleft()
                
        val = ""
        while s and not (s[0] == '(' or s[0] == ')'):
            val += s.popleft()
            
        if not val:
            return None
        
        cur = TreeNode(val)

        cur.left = self.helper(s)
        cur.right = self.helper(s)
        s.popleft()
             
        return cur 