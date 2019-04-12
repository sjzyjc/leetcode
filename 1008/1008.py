class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        for index in range(1, len(preorder)):
            node = TreeNode(preorder[index])
            self.insert(root, node)
            
        return root
    
    def insert(self, root, node):
        if not root:
            return node
        
        if node.val < root.val:
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)
            
        return root