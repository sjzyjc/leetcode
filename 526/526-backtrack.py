class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        used = [False for i in range(N)]
        self.counter = 0
        self.count(N, 1, used)
        return self.counter
        
    def count(self, N, pos, used):
        if pos == N + 1:
            self.counter += 1
            
        for i in range(1, N + 1):
            if not used[i - 1] and (i % pos == 0 or pos % i == 0):
                used[i - 1] = True
                self.count(N, pos + 1, used)
                used[i - 1] = False
                
            
    
            