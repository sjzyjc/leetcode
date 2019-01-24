class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        cur_level = next_level = 0
        step = 0
        for index, num in enumerate(nums):
            if index <= cur_level:
                next_level = max(next_level, index + num)
            else:
                step += 1
                cur_level = next_level
                next_level = index + num
                           
        return step