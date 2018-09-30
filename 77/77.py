class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    
    """
    def combine(self, n, k):
        # write your code here
        if n < 1 or k < 1:
            return []
        
        ans = []
        self.helper(n, k, 1, [], ans)
        return ans
        
    def helper(self, n, remain_count, start_num, carry, ans):
        if remain_count == 0:
            ans.append(carry + [])
            return
            
        for i in range(start_num, n + 1):
            carry.append(i)
            self.helper(n, remain_count - 1, i + 1, carry, ans)
            carry.pop()
            
            
            