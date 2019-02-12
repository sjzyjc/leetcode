import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        T: klogk
        """
        if not matrix or not matrix[0]:
            return 0
        
        heap = []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        visited = [[False for j in range(len(matrix[i]))] for i in range(len(matrix))]
        visited[0][0] = True
        
        ans = heap[0]
        
        for _ in range(k):
            ans, i, j = heapq.heappop(heap)
            
            if i + 1 < len(matrix) and not visited[i+1][j]:
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
                visited[i+1][j] = True
                
            if j + 1 < len(matrix[0]) and not visited[i][j+1]:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
                visited[i][j+1] = True
                
        return ans