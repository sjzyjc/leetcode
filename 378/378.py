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
        
        array = []
        for row in matrix:
            array.extend(row)
            
        self.quickSelect(array, k-1, 0, len(array) - 1)
        return array[k-1]
    
    def quickSelect(self, array, index, start, end):
        if start >= end:
            return
        
        left, right = start, end
        pivot = array[(start + end) // 2]

        while left <= right:
            while left <= right and array[left] < pivot:
                left += 1
                
            while left <= right and array[right] > pivot:
                right -= 1
            
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        
        if index <= right:
            self.quickSelect(array, index, start, right)
        
        if index >= left:
            self.quickSelect(array, index, left, end)
            
        
        