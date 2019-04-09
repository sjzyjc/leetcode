class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        width = len(matrix[0])
        
        while start <= end:
            mid = (start + end) // 2
            val = matrix[mid // width][mid % width] 
            if val == target:
                return True
            
            elif val < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return False
            
        