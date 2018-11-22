class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        
        return self.dfs(t)[1:-1]
    
    def dfs(self, t):
        if t is None:
            return ""
        
        left_str = self.dfs(t.left)
        right_str = self.dfs(t.right)
        
        if len(right_str) != 0 and len(left_str) == 0:
            left_str = "()"
        
        return "(" + str(t.val) + left_str + right_str + ")"
        
        