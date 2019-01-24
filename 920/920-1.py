MOD = 10 ** 9 + 7
class Solution:
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        if N is None or L is None or K is None:
            return 0
        
        f = [0 for j in range(N + 1)]
        f[0] = 1
        
        for i in range(1, L + 1):
            for j in range(min(i, N), -1, -1):
                f[j] = f[j] * max(0, j - K)
                if j >= 1:
                    f[j] += f[j - 1] * (N - j + 1) 
                
                f[j] %= MOD
                            
        return f[N]