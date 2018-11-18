# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N <= 0:
            return []
        
        if N == 1:
            node = TreeNode(0)
            return [node]
        
        if N % 2 == 0:
            return []
        
        left_no = 0
        ans = []

        while left_no <= N - 1:
            left_set = self.allPossibleFBT(left_no)
            right_set = self.allPossibleFBT(N - 1 - left_no)
        
            for left in left_set:
                for right in right_set:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ans.append(root)
            
            left_no += 1
                
        return ans
            