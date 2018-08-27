class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        for row in matrix:
            if target >= row[0] and target <= row[len(row) - 1]:
                return self.binarySearch(row, target)

        return False

    def binarySearch(self, row, target):
        start, end  = 0, len(row) - 1
        while start < end:
            mid = start + (end - start) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return row[start] == target       