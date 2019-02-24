class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        min(m,n)*log(mn)
        """
        if not m or not n or not k:
            return 0
        
        if m < 0 or n < 0:
            return 0
        
        start, end = 0, m*n
        while start < end:
            mid = (start + end) // 2
            if self.findLe(min(m,n), max(m, n), mid) < k:
                start = mid + 1
            else:
                end = mid
                
        return start
    
    def findLe(self, row, col, target):
        ans = 0
        for row_no in range(1, row + 1):
            ans += min(col, target // row_no)
            
        return ans
              
            
            