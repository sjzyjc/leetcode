class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return []
        
        i_len = len(A)
        j_len = len(A[0])
        k_len = len(B[0])
        ans = [[0 for _ in range(k_len)] for _ in range(i_len)]
        
        B_non_zero = []
        
        for j in range(j_len):
            row = []
            for k in range(k_len):
                if B[j][k] != 0:
                    row.append(k)
                    
            B_non_zero.append(row)
                    
        for i in range(i_len):
            for j in range(j_len):
                if A[i][j] == 0:
                    continue
                    
                for k in B_non_zero[j]:
                    ans[i][k] += A[i][j] * B[j][k]
                    
        return ans