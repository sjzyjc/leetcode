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
        f = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(2)]
        pre, cur = 0, 1
        
        for index, strr in enumerate(strs):
            for char in strr:
                if char == "0":
                    count_0[index] += 1
                elif char == "1":
                    count_1[index] += 1
        
        
        for i in range(1, len(strs) + 1):
            for j in range(m + 1):
                for k in range(n + 1):
                    f[cur][j][k] = f[pre][j][k]
                    
                    if j >= count_0[i - 1] and k >= count_1[i - 1]:
                        f[cur][j][k] = max(f[cur][j][k], f[pre][j - count_0[i - 1]][k - count_1[i - 1]] + 1)
            
            pre, cur = cur, pre
                        

        #print(f)
        return f[pre][-1][-1]