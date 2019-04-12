class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix or matrix[0] is None:
            return False
        
        row = len(matrix) - 1         
        for col in range(len(matrix[0])):  
            if not self.checker(row, col, matrix[row][col], matrix):
                return False
                
        col = len(matrix[0]) - 1
        for row in range(len(matrix) - 1, -1, -1):
            if not self.checker(row, col, matrix[row][col], matrix):
                return False
                
        return True
    
    def checker(self, row, col, base, matrix):
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            if matrix[row][col] != base:
                return False
                
            row -= 1
            col -= 1
            
        return True
        