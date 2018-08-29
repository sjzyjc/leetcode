# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        parent_sum = 0
        self.total_sum = 0
        self.dfs(root, parent_sum)
        return self.total_sum

    def dfs(self, node, parent_sum):
        if not node:
            return

        current_sum =  parent_sum * 10 + node.val  
        if node.left is None and node.right is None:
            self.total_sum += current_sum

        self.dfs(node.left, current_sum)
        self.dfs(node.right, current_sum)
         

sl = Solution()
a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
a.left = b
b.right = c

print(sl.sumNumbers(a))  