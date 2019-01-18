class Solution:
    def shoppingOffers(self, price, special, needs):
        memo = {}
        for index, val in enumerate(price):
            tmp = [0] * (len(needs) + 1)
            tmp[index] = 1
            tmp[-1] = val
            special.append(tmp)
        
        return self.dfs(needs, special, memo)
    
    def dfs(self, cur, special, memo):
        if tuple(cur) in memo:
            return memo[tuple(cur)]
        
        ans = (1 << 31) - 1 #cost without special
        for spec in special:
            tmp = [cur[j] - spec[j] for j in range(len(cur))]
            if min(tmp) < 0: 
                continue# skip deals that exceed needs
            ans = min(ans, self.dfs(tmp, special, memo) + spec[-1]) 
        
        memo[tuple(cur)] = ans
        return ans