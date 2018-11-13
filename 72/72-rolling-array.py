class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        
        if not word2:
            return len(word1)
        
        f = [[0 for j in range(len(word2) + 1)] for i in range(2)]
        prev, cur = 1, 0
        
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    f[cur][j] = j
                    continue
                    
                if j == 0:
                    f[cur][j] = i
                    continue
                    
                f[cur][j] = min(f[cur][j-1] + 1, f[prev][j] + 1, f[prev][j-1] + 1)
                if word1[i - 1] == word2[j - 1]:
                    f[cur][j] = min(f[cur][j], f[prev][j-1])
            
            prev, cur = cur, prev
                    
                
        return f[prev][-1]