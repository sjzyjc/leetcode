class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount:
            return 1
        
        if not coins:
            return 0
        
        f = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        f[0][0] = 1
        
        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                for k in range(j // coins[i - 1] + 1):
                    f[i][j] += f[i - 1][j - k * coins[i - 1]]
                    
                    
        return f[-1][-1]
        
        
        

    