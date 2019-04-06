DIRS = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if N is None or K is None:
            return 0
        
        
        f = [[[0.0 for _ in range(N)] for _ in range(N)] for _ in range(2)]
        prev, cur = 0, 1
        f[prev][r][c] = 1.0
        ans = 0
        
        for k in range(1, K + 1):
            for i in range(N):
                for j in range(N):
                    f[cur][i][j] = 0.0
                    
                    for direction in DIRS:
                        new_i = i - direction[0]
                        new_j = j - direction[1]
                        if not (0 <= new_i < N and 0 <= new_j < N):
                            continue
                            
                        f[cur][i][j] += (f[prev][new_i][new_j] * (1 / 8))
            
            prev, cur = cur, prev
                    
            
        for i in range(N):
            for j in range(N):
                ans += f[prev][i][j]
        
        return ans
        
        

                        
                    
            