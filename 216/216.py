class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if not k or not n:
            return []
        
        ans = []
        self.helper(k, n, 1, [], ans)
        return ans
    
    def helper(self, remain_count, remain, start_num, carry, ans):
        if remain == 0 and remain_count == 0:
            ans.append(carry + [])
            return
        
        if remain == 0 or remain_count == 0:
            return
        
        for i in range(start_num, 10):
            if i > remain:
                break
                
            carry.append(i)
            self.helper(remain_count - 1, remain - i, i + 1, carry, ans)
            carry.remove(i)
        