class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None

        return self.constuctTree(nums, 0, len(nums)-1)

    def constuctTree(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        node =  TreeNode(nums[mid])
        node.left = self.constuctTree(nums, start, mid - 1)
        node.right = self.constuctTree(nums, mid+1, end)

        return node
        
        
        
