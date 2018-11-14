# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        
        while queue:
            count = len(queue)
            total = 0
            
            for i in range(count):
                node = queue.popleft()
                total += node.val
                
                if node.left is not None:
                    queue.append(node.left)
                
                if node.right is not None:
                    queue.append(node.right)
                
            ans.append(total/count)
            
        return ans
            
                