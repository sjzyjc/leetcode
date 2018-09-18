class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        
        if not coins:
            return 0
            
        f = [0 for i in range(amount + 1)]
        f[0] = 0
        MAX = (1 << 31) - 1
        
        for i in range(1, amount + 1):
            f[i] = MAX
            
            for coin in coins:
                if i >= coin and f[i - coin] < MAX:
                    f[i] = min(f[i], f[i - coin] + 1)
        
        if f[amount] == MAX:
            return -1
        else:
            return f[amount] 