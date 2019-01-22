# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans = []
        self.helper(root, ans)
        return ans
    
    def helper(self, node, ans):
        if node is None:
            return -1
        
        left_len = self.helper(node.left, ans)
        right_len = self.helper(node.right, ans)
        
        cur_len = max(left_len, right_len) + 1
        if cur_len == len(ans):
            ans.append([])
        
        ans[cur_len].append(node.val)
        
        
        return cur_len
        