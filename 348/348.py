class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.col_count = [0 for _ in range(n)]
        self.row_count = [0 for _ in range(n)]
        self.dia_count = [0 for _ in range(2)]
        self.game_over = False
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if self.game_over:
            return -1
        
        if player == 1:
            self.col_count[col] += 1
            self.row_count[row] += 1
            
            if col == row:
                self.dia_count[0] += 1
            
            if col + row == len(self.col_count) - 1:
                self.dia_count[1] += 1
            
        else:
            self.col_count[col] -= 1
            self.row_count[row] -= 1
            
            if col == row:
                self.dia_count[0] -= 1
            
            if col + row == len(self.col_count) - 1:
                self.dia_count[1] -= 1
            
        #for col in self.grid:
            #print(col)
        #print("----------", self.findWin())
        winner = self.findWin()
        if winner != 0:
            self.game_over = True
            
        return winner
        
    def findWin(self):
        n = len(self.row_count)
        for i in range(n):
            row = self.row_count[i]
            col = self.col_count[i]
            if row == n or col == n:
                return 1
            
            if row == -n or col == -n:
                return 2
        
        if self.dia_count[0] == n or self.dia_count[1] == n:
            return 1
        
        if self.dia_count[0] == -n or self.dia_count[1] == -n:
            return 2
        
        return 0
            

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)