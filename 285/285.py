class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        next_node = None
        while root:
            if root is None:
                return None
            
            if root.val == p.val:
                break
            elif root.val < p.val:
                root = root.right
            else:
                next_node = root
                root = root.left
        
        if root.right:
            root = root.right
            while root.left:
                root = root.left
                
            return root
    
        return next_node