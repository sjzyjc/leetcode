from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return None
        
        used = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    self.add(i, j, board[i][j], used)

        #i, j is to be filled
        self.helper(board, 0, used)
        
        
    def add(self, i, j, value, used):
        #0-8 for rows
        used[i].add(value)
        #9 - 17 for cols
        used[9 + j].add(value)
        #18 - 26 for sqaures
        used[18 + i // 3 * 3 + j // 3].add(value)
        
    def remove(self, i, j, value, used):
        used[i].remove(value)
        used[9 + j].remove(value)          
        used[18 + i // 3 * 3 + j // 3].remove(value)
        
    
    def helper(self, board, pos, used):
        if pos >= 81:
            return True
        
        i = pos // 9
        j = pos % 9
        if board[i][j] != '.':
            return self.helper(board, pos + 1, used)
        else:
            for num in range(1, 10):
                num = str(num)
                if num in used[i] or num in used[9 + j] or num in used[18 + i // 3 * 3 + j //3]:
                    continue
                    
                board[i][j] = num
                self.add(i, j, num, used)
                if self.helper(board, pos + 1, used):
                    return True
                    
                self.remove(i, j, num, used)
                board[i][j] = '.'
                        
        return False
                