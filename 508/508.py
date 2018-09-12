# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        self.freq_map = {}
        self.helper(root)
        max_len = max(self.freq_map.values())
        ans = []
        
        for i in self.freq_map:
            if self.freq_map[i] == max_len:
                ans.append(i)
                
        return ans
    
    def helper(self, root):
        if root is None:
            return 0
        
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        
        total = left_sum + right_sum + root.val
        if total not in self.freq_map:
            self.freq_map[total] = 1
        else:
            self.freq_map[total] += 1
            
        return total