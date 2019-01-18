# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None

        s = '(' + s + ')'
        stack = []
        ptr = 0

        while ptr < len(s):
            char = s[ptr]

            if char == ')':
                node = stack.pop()
                
                if stack:
                    if stack[-1].left is None:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                        
            elif char.isdigit() or char == '-':
                val = ""
                while ptr < len(s) and (s[ptr].isdigit() or s[ptr] == '-'):
                    val += s[ptr]
                    ptr += 1
                
                node  = TreeNode(int(val))
                stack.append(node)
                continue
            
            ptr += 1
            
        return node if node else None
            