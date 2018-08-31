from collections import deque
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None
        
        root = TreeNode(nums[(0 + len(nums)-1) // 2])
        queue = deque()
        queue.append([root, 0, len(nums)-1])
        
        while queue:
            node, start, end = queue.popleft()
            if node is None:
                continue

            if start >= end:
                continue  

            mid = (start + end) // 2
            if start == mid:
                node.left = None
            else:    
                node.left = TreeNode(nums[(start + mid - 1) // 2])
            node.right = TreeNode(nums[(mid + 1 + end) // 2])

            queue.append([node.left, start, mid -1])
            queue.append([node.right, mid + 1, end])

        return root 