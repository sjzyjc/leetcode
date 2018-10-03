class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n or n <= 0:
            return []
        
        pos = []
        self.count = 0
        self.find(n, pos)
        return self.count
    
    def find(self, n, pos):
        if len(pos) == n:
            self.count += 1
            return
        
        for col in range(n):
            if not self.isValid(col, pos):
                continue
            
            pos.append(col)
            self.find(n, pos)
            pos.pop()
            
    
    def isValid(self, col, pos):
        for row_index in range(len(pos)):
            col_index = pos[row_index]
            if col_index == col:
                return False
            
            if col_index + row_index == len(pos) + col:
                return False
            
            if col_index - row_index == col - len(pos):
                return False
            
        return True
            