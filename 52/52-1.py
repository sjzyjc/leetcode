class Solution:
    def totalNQueens(self, n: int) -> int:
        if not n:
            return 0
        
        cols = set()
        diag_1 = set()
        diag_2 = set()
        return self.permute(0, n, cols, diag_1, diag_2)
        
    
    def permute(self, row, n, cols, diag_1, diag_2):
        if row == n:
            return 1
        
        ans = 0
        for i in range(n):
            if i in cols or row + i in diag_1 or row - i in diag_2:
                continue
            
            diag_1.add(row + i)
            diag_2.add(row - i)
            cols.add(i)
            ans += self.permute(row + 1, n, cols, diag_1, diag_2)
            cols.remove(i)
            diag_1.remove(row + i)
            diag_2.remove(row - i)
            
        return ans
            
            
            
            
        