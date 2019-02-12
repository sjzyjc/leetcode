import heapq
OFFSETS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0] or len(heightMap) == 1 or len(heightMap[0]) == 1:
            return 0
        
        heap = []
        visited = [[False for _ in range(len(heightMap[0]))] for _ in range(len(heightMap))]
        for i in range(len(heightMap)):
            for j in range(len(heightMap[i])):
                if i == 0 or i == len(heightMap) - 1 or j == 0 or j == len(heightMap[0]) - 1:
                    visited[i][j] = True
                    heapq.heappush(heap, (heightMap[i][j], i, j))
        
        ans = 0
        while heap:
            edge_water_level, i, j = heapq.heappop(heap)
            for offset in OFFSETS:
                new_i = i + offset[0]
                new_j = j + offset[1]
                if not (0 <= new_i < len(heightMap) and 0 <= new_j < len(heightMap[0])):
                    continue
                    
                if visited[new_i][new_j]:
                    continue
                    
                visited[new_i][new_j] = True
                new_water_level = max(edge_water_level, heightMap[new_i][new_j])
                ans += max(0, edge_water_level - heightMap[new_i][new_j])
                heapq.heappush(heap, (new_water_level, new_i, new_j))
                
        return ans
                
                
        