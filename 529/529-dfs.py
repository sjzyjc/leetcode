OFFSETS = [[1, 0], [1, -1], [1, 1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1]]
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return board
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        self.dfs(board, click[0], click[1])
        return board
        
    def dfs(self, board, i, j):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return 
        
        if board[i][j] != 'E':
            return
        
        count = self.getMines(board, i, j)
        if count == 0:
            board[i][j] = 'B'
            for offset in OFFSETS:
                self.dfs(board, i + offset[0], j + offset[1])
        else:
            board[i][j] = str(count)
            
    def getMines(self, board, i, j):
        count = 0
        for offset in OFFSETS:
            new_i = i + offset[0]
            new_j = j + offset[1]
            if not (0 <= new_i < len(board) and 0 <= new_j < len(board[0])):
                continue
                
            if board[new_i][new_j] == 'M':
                count += 1
                
        return count