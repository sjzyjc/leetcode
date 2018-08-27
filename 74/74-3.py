class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        row_index = self.findRow(matrix, target)
        if row_index == -1
            return False

        return self.binarySearch(matrix[row_index], target)

    def findRow(self, matrix, target):
        start, end = 0, len(matrix) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid][0] > target:
               end = mid - 1
            else:
               start = mid    

        last_index = len(matrix[0]) - 1
        if traget <= matrix[end][last_index] and target >= matrix[end][0]:
            return end
        elif target < matrix[end][0] and target >= matrix[start][0]:
            return start
        else:
            return -1    

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