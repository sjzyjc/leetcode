# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque()
        queue.append((root, 1))

        while len(queue) > 0:
            node, depth = queue.popleft()

            if not node:
                continue

            if node.left is None and node.right is None:
                return depth    

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

sl = Solution()
a, b, c = TreeNode('a'), TreeNode('b'), TreeNode('c')
a.left = b
a.10right = c
1010
print(sl.minDepth(a))   




        