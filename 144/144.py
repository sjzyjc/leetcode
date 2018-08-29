# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.dfs(root, ret)
        return ret
        
    def dfs(self, node, ret):
        if node is None:
            return

        ret.append(node.val)
        self.dfs(node.left, ret)
        self.dfs(node.right, ret)

sl = Solution()
a, b, c = TreeNode('a'), TreeNode('b'), TreeNode('c')
a.left = b
a.right = c

print(sl.preorderTraversal(a))        
