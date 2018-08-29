# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.getSubTreeDepth(root) != -1


        
    def getSubTreeDepth(self, node):
        if node is None:
            return 0

        left_depth = self.getSubTreeDepth(node.left) 
        right_depth = self.getSubTreeDepth(node.right) 

        if left_depth == -1 or right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        return max(left_depth, right_depth) + 1



sl = Solution()
a, b, c = TreeNode('a'), TreeNode('b'), TreeNode('c')
a.left = b
a.right = c

print(sl.isBalanced(a))            

            
            