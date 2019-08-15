class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        return self.dfs(n, set())
        
    def dfs(self, n, visited):
        if n == 1:
            return True
        
        if n in visited:
            return False
        
        visited.add(n)
        tmp = 0
        while n > 0:
            tmp += (n % 10) * (n % 10)
            n = n // 10
            
        if self.dfs(tmp, visited):
            return True
        
        return False