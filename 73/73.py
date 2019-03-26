class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or matrix[0] is None:
            return 
        
        
        first_row = False
        first_col = False
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col = True
                break
                
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row = True
                break
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] != 0:
                    continue
                    
                matrix[i][0] = 0
                matrix[0][j] = 0
                
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
                    
        #print(first_col)
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                
        
        if first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0