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
        
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)] 

        
        for i in range(1, len(strs) + 1):
            count_0, count_1 = 0, 0
            for char in strs[i - 1]:
                if char == "0":
                    count_0 += 1
                elif char == "1":
                    count_1 += 1
                    
            for j in range(m, count_0 - 1 , -1):
                for k in range(n, count_1 - 1, -1):
                    f[j][k] = max(f[j][k], f[j - count_0][k - count_1] + 1)
            
                        

        #print(f)
        return f[-1][-1]