class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            []
            
        count = collections.defaultdict(int)
        ans = []
        self.dfs(root, count, ans)
        return list(ans)
    
    def dfs(self, node, count, ans):
        if not node:
            return "#"
        
        serialize = str(node.val) + self.dfs(node.left, count, ans) + self.dfs(node.right, count, ans)
        if count[serialize] == 1:
            ans.append(node)
        
        count[serialize] += 1
            
        return serialize
        
        