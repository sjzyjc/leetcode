class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        if not strs or m < 0 or n < 0:
            return 0
        
        count_0 = [0 for _ in range(len(strs))]
        count_1 = [0 for _ in range(len(strs))]
        f = [[[-1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                f[0][i][j] = 0
        
        for index, strr in enumerate(strs):
            for char in strr:
                if char == "0":
                    count_0[index] += 1
                elif char == "1":
                    count_1[index] += 1
        
        return self.helper(len(strs), m, n, count_0, count_1, f)
        
    
    def helper(self, i, m, n, count_0, count_1, f):
        if f[i][m][n] != -1:
            return f[i][m][n]
        
        tmp = self.helper(i - 1, m, n, count_0, count_1, f)
        if m >= count_0[i - 1] and n >= count_1[i - 1]:
            tmp = max(tmp, self.helper(i - 1, m - count_0[i - 1], n - count_1[i - 1], count_0, count_1, f) + 1)
            
        f[i][m][n] = tmp
        return f[i][m][n]
        