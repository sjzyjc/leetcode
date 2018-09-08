class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        
        while start < end:
            mid = start + (end - start) // 2
            tmp_sum = mid * (mid + 1) // 2
            if tmp_sum == n:
                return mid
            elif tmp_sum < n:
                start = mid + 1
            else:
                end = mid - 1
                
        if start * (start + 1) // 2 <= n:
            return start
        else:
            return start - 1
            
            
        
        