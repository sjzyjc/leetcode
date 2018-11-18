from collections import deque
class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(v)
        
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        
        queue = deque([root])
        depth = 1
        while depth < d - 1:
            depth += 1
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                if node is None:
                    continue
                    
                queue.append(node.left)
                queue.append(node.right)
                
        for node in queue:
            if node is None:
                continue
            
            new_left = TreeNode(v)
            new_right = TreeNode(v)
            
            orig_left = node.left
            orig_right = node.right
            
            node.left = new_left
            node.right = new_right
            
            new_left.left = orig_left
            new_right.right = orig_right
    
        return root
        
        