class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        index = self.findMaxIndex(nums)
        node = TreeNode(nums[index])
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index + 1:])
        
        return node
    
    def findMaxIndex(self, nums):
        maximum = -(1 << 31)
        ans = -1
        for index, num in enumerate(nums):
            if num > maximum:
                maximum = num
                ans = index
        return ans
        