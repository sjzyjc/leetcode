class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid = [['E' for _ in range(n)] for _ in range(n)]
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
            self.grid[row][col] = 'X'
        else:
            self.grid[row][col] = 'O'
            
        #for col in self.grid:
            #print(col)
        #print("----------", self.findWin())
        return self.findWin()
        
    def findWin(self):
        row_score = [0 for _ in range(len(self.grid))]
        col_score = [0 for _ in range(len(self.grid))]
        dia_score = [0 for _ in range(2)]
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 'X':
                    if i == j:
                        dia_score[0] +=1
                    if i + j == len(self.grid[i]) - 1:
                        dia_score[1] += 1
                    row_score[i] += 1
                    col_score[j] += 1
                elif self.grid[i][j] == 'O':
                    if i == j:
                        dia_score[0] -= 1
                    if i + j == len(self.grid[i]) - 1:
                        dia_score[1] -= 1
                    row_score[i] -= 1
                    col_score[j] -= 1
            
            if row_score[i] == len(self.grid):
                return 1
            
            if row_score[i] == -len(self.grid):
                return 2
        
        for score in col_score:
            if score == len(self.grid):
                return 1
            
            if score == -len(self.grid):
                return 2
        
        #print(dia_score)
        if dia_score[0] == len(self.grid) or dia_score[1] == len(self.grid):
            return 1
        
        if dia_score[0] == -len(self.grid) or dia_score[1] == -len(self.grid):
            return 2
        
        return 0
            

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)