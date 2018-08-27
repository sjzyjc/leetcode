class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        num_list = []
        for row in matrix:
            num_list += row

        start, end = 0, len(num_list) - 1

        while start < end:
            mid  = start + (end - start) // 2
            if num_list[mid] == target:
                return True
            elif num_list[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return num_list[start] == target  