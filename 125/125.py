class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        level_map = {}
        self.dfs(root, level_map, -1) 

        ret = []
        for i in range(len(level_map)):
            ret.append(level_map[i])

        return ret    

    def dfs(self, node, level_map, prev_level):
        if not node:
            return

        cur_level = prev_level + 1
        level_map [cur_level] = node.val
        self.dfs(node.left, level_map, cur_level)
        self.dfs(node.right, level_map, cur_level)


sl = Solution()
a, b, c = TreeNode('a'), TreeNode('b'), TreeNode('c')
a.left = b
b.right = c

print(sl.rightSideView(a))  

        