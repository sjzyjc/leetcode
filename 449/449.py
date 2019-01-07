# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(str(node.val))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return ",".join(ans)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #print(data)
        if not data:
            return None
        
        #2, 1, 1.5 vs 4, 2, 1, 3
        data = data.split(",")
        root = node = TreeNode(int(data[0]))
        stack = [node]
        
        for i in range(1, len(data)):
            new_node = TreeNode(int(data[i]))
            if new_node.val <= node.val:
                node.left = new_node
            
            else:
                while stack and new_node.val > stack[-1].val:
                    node = stack.pop()
                
                node.right = new_node
            
            node = new_node
            stack.append(new_node)
            
        return root
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))