class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        
        top = 0 
        bottom = len(matrix) - 1
        while top < bottom:
            for j in range(len(matrix)):
                #print(top, bottom, j)
                matrix[top][j], matrix[bottom][j] = matrix[bottom][j], matrix[top][j]
                
            top += 1
            bottom -= 1
        
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]