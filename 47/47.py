class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        
        ans = []
        visited = [False for i in range(len(nums))]
        nums.sort()
        self.permute(nums, [], visited, ans)
        return ans
    
    def permute(self, nums, carry, visited, ans):
        if len(carry) == len(nums):
            ans.append(carry + [])
            return
        
        for index in range(len(nums)):
            if visited[index]:
                continue
            
            if index > 0 and nums[index] == nums[index - 1] and not visited[index - 1]:
                continue
                
            visited[index] = True
            carry.append(nums[index])
            self.permute(nums, carry, visited, ans)
            carry.pop()
            visited[index] = False
        
            