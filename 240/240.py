class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
             high       
        left      right
            low
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0: 
            return False

        height, width = len(matrix), len(matrix[0])
        row = 0
        col = width - 1

        while row <= height - 1 and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target: 
                row += 1
            else:
                col -= 1
                
        return False