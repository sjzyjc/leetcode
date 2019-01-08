from collections import deque
class Solution:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        queue = [(self.getVal(nums[0]), self.getId(nums[0]))]
        
        i = 1
        cur_level = 1
        ans = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                prefix_sum, cur_id = queue.pop()
                
                child_count = 0
                while i < len(nums) and self.getLevel(nums[i]) == cur_level + 1 and self.getParentId(nums[i]) == cur_id:
                    queue.append((prefix_sum + self.getVal(nums[i]), self.getId(nums[i])))
                    child_count += 1
                    i += 1
                    
                if child_count == 0:
                    ans += prefix_sum
                    
            cur_level += 1
            
        return ans
                    
                  
    def getLevel(self, num):
        return num // 100
        
    def getId(self, num):
        return (num % 100) // 10
        
    def getVal(self, num):
        return num % 10
    
    def getParentId(self, num):
        return (self.getId(num) - 1) // 2 + 1
                    
                                       
                
            
        