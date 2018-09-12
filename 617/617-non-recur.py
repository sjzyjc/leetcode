# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        
        q1 = deque([t1, None])
        q2 = deque([t2, None])
        
        while q1 or q2:
            node1 = q1.pop()
            node2 = q2.pop()
            
            if not node1 or not node2:
                continue
                
            if node1 is not None and node2 is not None:
                node1.val += node2.val

            if node1.left is None:
                node1.left = node2.left
            else:
                q1.append(node1.left)
                q2.append(node2.left)
                
            if node1.right is None:
                node1.right = node2.right
            else:
                q1.append(node1.right)
                q2.append(node2.right)
                
        return t1
                            