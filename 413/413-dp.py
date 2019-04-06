class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A:
            return 0
        
        if len(A) < 3:
            return 0
        
        f = [0 for _ in range(len(A))]
        ans = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                f[i] = f[i - 1] + 1
                
            ans += f[i]
                
        return ans
                
                
                
        
                
                
                
        