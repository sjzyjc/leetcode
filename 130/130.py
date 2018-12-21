class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        O(N^2)
        """
        if not board or not board[0]:
            return
        
        for i in range(len(board)):
            for j in [0, len(board[0]) - 1]:
                if board[i][j] == "X" or board[i][j] == "+":
                    continue
                self.dfs(board, i, j)
            
            
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                if board[i][j] == "X" or board[i][j] == "+":
                    continue
                self.dfs(board, i, j)
                
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "+":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                    
    def dfs(self, board, i, j):
        if not (0 <= i < len(board) and 0 <= j < len(board[i])):
            return
        
        if board[i][j] == "X" or board[i][j] == "+":
            return
        
        board[i][j] = "+"
        offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for offset in offsets:
            self.dfs(board, i + offset[0], j + offset[1])
            
                
            
            