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

        level_map = []
        self.dfs(root, level_map, -1) 

        return level_map    

    def dfs(self, node, level_map, prev_level):
        if not node:
            return

        cur_level = prev_level + 1
        if len(level_map) - 1 < cur_level:
            level_map.append(node.val)
        else:   
            level_map[cur_level] = node.val 

        self.dfs(node.left, level_map, cur_level)
        self.dfs(node.right, level_map, cur_level)

sl = Solution()
a, b, c = TreeNode('a'), TreeNode('b'), TreeNode('c')
a.left = b
a.right = c

print(sl.rightSideView(a))  

        