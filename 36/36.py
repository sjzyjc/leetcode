class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board or not(board[0]):
            return False
        
        for i in range(9):
            if not self.isValid(board, i, i, 0, 8):
                return False
            
            if not self.isValid(board, 0, 8, i, i):
                return False
            
        
        for i in range(3):
            for j in range(3):
                if not self.isValid(board, i * 3, i * 3 + 2, j * 3, j * 3 + 2):
                    return False
                
        return True
            
    
    def isValid(self, board, i_lo, i_high, j_lo, j_high):
        hashset = set()
        for i in range(i_lo, i_high + 1):
            for j in range(j_lo, j_high + 1):
                if board[i][j] == '.':
                    continue
                    
                if board[i][j] in hashset:
                    return False
                
                hashset.add(board[i][j])
                
        return True
        