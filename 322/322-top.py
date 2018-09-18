class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        
        self.MAX = (1 << 31) - 1
        arr = [0] + [-1 for i in range(amount)]
        self.helper(coins, amount, arr)
        if arr[amount] == self.MAX:
            return -1
        else:
            return arr[amount]
        
    def helper(self, coins, amount, arr):
        if amount < 0:
            return self.MAX
        
        if arr[amount] != -1:
            return arr[amount]
        
        ans = self.MAX
        for coin in coins:
            ans = min(ans, self.helper(coins, amount - coin, arr) + 1)
        
        arr[amount] = ans
        return ans