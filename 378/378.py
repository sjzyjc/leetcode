class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        T: MN
        """
        if not matrix or not matrix[0]:
            return 0
            
        self.quickSelect(matrix, k-1, 0, len(matrix) * len(matrix[0]) - 1)
        return matrix[(k-1) // len(matrix[0])][(k-1) % len(matrix[0])]
    
    def quickSelect(self, array, index, start, end):
        if start >= end:
            return
        
        pivot_x = ((start + end) // 2) // len(array[0])
        pivot_y = ((start + end) // 2) % len(array[0])

        left, right = start, end
        pivot = array[pivot_x][pivot_y]
        left_x = left // len(array[0])
        left_y = left % len(array[0])
        right_x = right // len(array[0])
        right_y = right % len(array[0])
        while left <= right:
            
            while left <= right and array[left_x][left_y] < pivot:
                left += 1
                left_x = left // len(array[0])
                left_y = left % len(array[0])
            
            while left <= right and array[right_x][right_y] > pivot:
                right -= 1
                right_x = right // len(array[0])
                right_y = right % len(array[0])
                
            
            if left <= right:
                array[left_x][left_y], array[right_x][right_y] = array[right_x][right_y], array[left_x][left_y]
                left += 1
                right -= 1
                left_x = left // len(array[0])
                left_y = left % len(array[0])
                right_x = right // len(array[0])
                right_y = right % len(array[0])
        
        if index <= right:
            self.quickSelect(array, index, start, right)
        
        if index >= left:
            self.quickSelect(array, index, left, end)
            
        
        