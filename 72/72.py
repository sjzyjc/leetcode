class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 is None:
            return len(word2)
        
        if word2 is None:
            return len(word1)
        
        f = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        
        for i in range(len(word1) + 1):
            f[i][0] = i
            
        for j in range(len(word2) + 1):
            f[0][j] = j
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                f[i][j] = min(f[i][j-1] + 1, f[i-1][j] + 1, f[i-1][j-1] + 1)
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i][j], f[i-1][j-1])
                    
                
        return f[-1][-1]