class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        
        visited = [False for _ in range(len(M))]
        ans = 0
        for i in range(len(M)):
            if visited[i]:
                continue
                
            self.dfs(M, i, visited)
            ans += 1
            
        return ans
    
    def dfs(self, M, i, visited):
        if visited[i]:
            return
        
        visited[i] = True
        for j in range(len(M[i])):
            if M[i][j] == 0:
                continue
            
            self.dfs(M, j, visited)
            
        