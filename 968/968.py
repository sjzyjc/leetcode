# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return min(self.dfs(root)[0], self.dfs(root)[1])
            
    def dfs(self, node):
        if not node:
            return (1 << 31) - 1, 0, 0
        
        l_covered_with_cam, l_covered_without_cam, l_not_covered = self.dfs(node.left)
        r_covered_with_cam, r_covered_without_cam, r_not_covered = self.dfs(node.right)
        
        covered_with_cam = min(l_covered_with_cam, l_covered_without_cam, l_not_covered) + min(r_covered_with_cam, r_covered_without_cam, r_not_covered) + 1
        
        covered_without_cam = min(l_covered_with_cam + min(r_covered_with_cam, r_covered_without_cam), r_covered_with_cam + min(l_covered_with_cam, l_covered_without_cam))
        
        not_covered = l_covered_without_cam + r_covered_without_cam
        
        return covered_with_cam, covered_without_cam, not_covered

        