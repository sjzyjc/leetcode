class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return None
        
        #i, j is to be filled
        self.helper(board, 0)
        
    
    def helper(self, board, pos):
        if pos >= 81:
            return True
        
        i = pos // 9
        j = pos % 9
        if board[i][j] != '.':
            return self.helper(board, pos + 1)
        else:
            for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                board[i][j] = num
                if self.validate(board, i, i, 0, 8) and self.validate(board, 0, 8, j, j) and self.validate(board, i // 3 * 3, i // 3 * 3 + 2, j // 3 * 3, j // 3 * 3 + 2):
                    res = self.helper(board, pos + 1)
                    
                    if res:
                        return True
                    
                board[i][j] = '.'
                        
        return False
        
    def validate(self, board, i_low, i_high, j_low, j_high):
        hashset = set()
        for i in range(i_low, i_high + 1):
            for j in range(j_low, j_high + 1):
                if board[i][j] == '.':
                    continue
                    
                if board[i][j] in hashset:
                    return False
                
                hashset.add(board[i][j])
                
        return True
                class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return None
        
        #i, j is to be filled
        self.helper(board, 0)
        
    
    def helper(self, board, pos):
        if pos >= 81:
            return True
        
        i = pos // 9
        j = pos % 9
        if board[i][j] != '.':
            return self.helper(board, pos + 1)
        else:
            for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                board[i][j] = num
                if self.validate(board, i, i, 0, 8) and self.validate(board, 0, 8, j, j) and self.validate(board, i // 3 * 3, i // 3 * 3 + 2, j // 3 * 3, j // 3 * 3 + 2):
                    res = self.helper(board, pos + 1)
                    
                    if res:
                        return True
                    
                board[i][j] = '.'
                        
        return False
        
    def validate(self, board, i_low, i_high, j_low, j_high):
        hashset = set()
        for i in range(i_low, i_high + 1):
            for j in range(j_low, j_high + 1):
                if board[i][j] == '.':
                    continue
                    
                if board[i][j] in hashset:
                    return False
                
                hashset.add(board[i][j])
                
        return True
                