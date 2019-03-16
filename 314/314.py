# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        location = defaultdict(list)
        
        queue = deque([(root, 0)])
        while queue:
            node, x = queue.popleft()
            location[x].append(node.val)
            
            if node.left:
                queue.append((node.left, x - 1))
                
            if node.right:
                queue.append((node.right, x + 1))
                
        
        return [location[i] for i in sorted(location)]
        
        