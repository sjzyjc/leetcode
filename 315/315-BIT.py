class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        since each time update only amend 1 no need to have the orignal arr
        """
        if not nums:
            return []
        
        max_num = max(nums)
        min_num = min(nums)
        size = max_num - min_num + 1
        self.bit = [0 for _ in range(size + 1)]
        
        ans = []
        for index in range(len(nums) - 1, -1, -1):
            num = nums[index]
            bit_index = num - min_num + 1
            self.update(bit_index)
            ans.append(self.prefixSum(bit_index - 1))
        
        return ans[::-1]
    
    def update(self, index):
        while index < len(self.bit):
            self.bit[index] += 1
            index += self.lowbit(index)
        
    def lowbit(self, i):
        return i & -i
    
    def prefixSum(self, index):
        ans = 0
        while index > 0:
            ans += self.bit[index]
            index -= self.lowbit(index)
            
        return ans
                
        