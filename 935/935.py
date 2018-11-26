from collections import defaultdict
class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if not N or N <= 0:
            return 0
        
        f = [[1 for _ in range(2)] for _ in range(10)]
        keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
        index = [[1, 2], [-1, -2], [2, 1], [-2, -1], [1, -2], [-1, 2], [2, -1], [-2, 1]]
        reach = defaultdict(list)
        for i in range(4):
            for j in range(3):
                val = keyboard[i][j]
                if val == -1:
                    continue
                
                for k in index:
                    if not (0 <= i + k[0] < 4 and 0 <= j + k[1] < 3):
                        continue
                        
                    next_step = keyboard[i + k[0]][j + k[1]]
                    if next_step == -1:
                        continue
                        
                    reach[val].append(next_step)
        
        pre, cur = 1, 0
        for j in range(2, N + 1):
            for i in range(10):
                f[i][cur] = 0
                for k in reach[i]:
                    f[i][cur] += f[k][pre] % (10 ** 9 + 7)
                
            pre, cur = cur, pre
                
                    
        
        #print(f)
        ans = 0
        for i in range(10):
            ans += (f[i][pre]  % (10 ** 9 + 7) )
            
        return ans % (10 ** 9 + 7)
                
                
                        
        