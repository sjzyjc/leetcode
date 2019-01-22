class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        if not piles:
            return False
        
        f = [[0 for j in range(len(piles))] for i in range(len(piles))]
        
        for i in range(len(piles)):
            f[i][i] = piles[i]
            
        for i in range(len(piles) - 1, -1, -1):
            for j in range(i + 1, len(piles)):
                f[i][j] = max(-f[i + 1][j] + piles[i], -f[i][j - 1] + piles[j])
   
        #print(f)
        return f[0][-1] > 0
                