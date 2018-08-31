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
        
        queue = deque()
        queue.append((root, 0))
        level_map = {}

        while queue:
            node, depth = queue.popleft()

            if not node:
                continue

            if depth not in level_map:
                level_map[depth] = [node.val]
            else:
                level_map[depth].append(node.val)    
            
            queue.append((node.left, depth+1))
            queue.append((node.right, depth+1))

        
        for i in level_map:
            if level_map[i] != level_map[i][::-1]:
                return False

        return True        
sl = Solution()
a, b, c = TreeNode('a'), TreeNode('b'), TreeNode('b')
a.left = b
a.right = c

print(sl.isSymmetric(a))       