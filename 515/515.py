# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = deque()
        queue.append((root, 0))
        ret = []
        current_level = -1
        
        while queue:
            node, depth = queue.popleft()
            if node is None:
                continue

            if depth == current_level:
                if node.val > ret[depth]:
                    ret[depth] = node.val

            elif depth > current_level:
                current_level = depth 
                ret.append(node.val)
        
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        return ret    

sl = Solution()
a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
a.left = b
b.right = c

print(sl.largestValues(a))   