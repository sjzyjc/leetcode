from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall or not wall[0]:
            return 0
        
        edge_count = defaultdict(int)
        for row in wall:
            edge = 0
            for index in range(len(row) - 1):
                edge += row[index]
                edge_count[edge] += 1
                
        ans = len(wall)
        for i in edge_count:
            ans = min(ans, len(wall) - edge_count[i])
            
        return ans
                
                
        