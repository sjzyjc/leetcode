import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0] or not k or k > len(matrix) * len(matrix[0]):
            return -1
        
        heap = []
        for index, row in enumerate(matrix):
            heapq.heappush(heap, (row[0], index, 0))
            
        for _ in range(k - 1):
            val, row_index, col_index = heapq.heappop(heap)
            
            if col_index + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[row_index][col_index + 1], row_index, col_index + 1))
                
        return heapq.heappop(heap)[0]