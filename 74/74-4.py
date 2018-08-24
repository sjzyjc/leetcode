class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        width = len(matrix[0])
        height = len(matrix)

        start, end = 0, height * width- 1
        while start < end:
            mid = start + (end - start) // 2

            row_index = mid // width
            column_index = mid % width
            
            if matrix[row_index][column_index] == target:
                return True
            elif matrix[row_index][column_index] < target:
                start = mid + 1
            else:
                end = mid - 1

        return matrix[start // width][start % width] == target         