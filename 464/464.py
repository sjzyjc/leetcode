class Solution:
    def canIWin(self, num, total):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if total <= 0:
            return True
        
        if num <= 0:
            return False
        
        if (num + 1) * num / 2 < total:
            return False
        
        memo = {}
        ans = self.helper([i for i in range(1, num + 1)], total, memo, 0)
        return ans
    
    def helper(self, nums, total, memo, pre_socre):
        if pre_socre >= total:
            return False
        
        state = str(nums)
        if state in memo:
            return memo[state]
        
        can_win = False
        for index, next_move in enumerate(nums):
            if self.helper(nums[:index] + nums[index + 1:], total, memo, pre_socre + next_move) is False:
                can_win = True
                break
                    
        memo[state] = can_win
        return can_win

            
            