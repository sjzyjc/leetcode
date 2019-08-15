class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A:
            return 0
        
        if len(A) < 3:
            return 0
        
        delta = A[1] - A[0]
        i = 0
        ans = 0
        for j in range(2, len(A) + 1):
            val = A[j] if j != len(A) else (1 << 31) - 1
            if val - A[j - 1] != delta:
                delta = val - A[j - 1]
                l = j - i
                ans += (l - 1) * (l - 2) // 2
                i = j - 1
                
        return ans
                