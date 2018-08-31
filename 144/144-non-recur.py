
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            if not node:
                continue

            ret.append(node.val)

            stack.append(node.right)
            stack.append(node.left)

        return ret