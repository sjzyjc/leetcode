class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or len(board) == 0 or len(board[0]) == 0:
            return False

        height, width = len(board), len(board[0])
        for i in range(height):
            for j in range(width):
                if self.find(board, i, j, 0, word):
                    return True

        return False           
        

    def find(self, board, i, j, word_index, word):
        if not (0<= i < len(board) and 0<= j < len(board[0])) or word_index > len(word) - 1 or board[i][j] != word[word_index]:
            return False

        if word_index == len(word) - 1:
            return True    
        
        word_index += 1
        char =  board[i][j]
        board[i][j] = '$'
        exsited = self.find(board, i + 1, j, word_index, word) or self.find(board, i - 1, j, word_index, word) or self.find(board, i, j+1, word_index, word) or self.find(board, i, j-1, word_index, word)
        board[i][j] = char
        
        return exsited