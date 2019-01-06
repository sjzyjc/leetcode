# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n or n <= 0:
            return []
        
        memo = {}
        return self.helper(1, n, memo)
    
    def helper(self, start, end, memo):
        if start > end:
            return [None]
            
        if (start, end) in memo:
            return memo[(start, end)]
        
        ans = []
        for i in range(start, end + 1):
            left_nodes = self.helper(start, i - 1, memo)
            right_nodes = self.helper(i + 1, end, memo)
            
            for left_node in left_nodes:
                for right_node in right_nodes:
                    node = TreeNode(i)
                    node.left = left_node
                    node.right = right_node
                    
                    ans.append(node)
                    
        memo[(start, end)] = ans
        #print(memo)
        return ans