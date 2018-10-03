# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left is None or right is None:
            return left is None and right is None
        
        if left.val != right.val:
            return False

        return self.check(left.left, right.right) and self.check(left.right, right.left)



sl = Solution()
a, b, c = TreeNode('a'), TreeNode('b'), TreeNode('b')
a.left = b
a.right = c

print(sl.isSymmetric(a))       