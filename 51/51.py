class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n:
            return []
        
        pos = []
        ans = []
        self.find(n, pos, ans)
        return ans
    
    def find(self, n, pos, ans):
        if len(pos) == n:
            ans.append(self.draw(pos))
            return
        
        for col in range(n):
            if not self.isValid(col, pos):
                continue
            
            pos.append(col)
            self.find(n, pos, ans)
            pos.pop()
            
    def draw(self, pos):
        ans = []
        for i in range(len(pos)):
            row = ""
            for j in range(len(pos)):
                if j != pos[i]:
                    row += '.'
                else:
                    row += 'Q'
                    
            ans.append(row)
        return ans
    
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
            