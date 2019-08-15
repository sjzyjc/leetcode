INT_MAX = (1 << 31) - 1
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points_set = set()
        ans = INT_MAX
        
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            
            points_set.add((x1, y1))
            for j in range(i + 1, len(points)):
                x2 = points[j][0]
                y2 = points[j][1]
                
                points_set.add((x2, y2))
                if x1 == x2 or y1 == y2:
                    continue
                    
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    ans = min(ans, abs(x2 - x1) * abs(y1 - y2))
                                        
        
        return ans if ans != INT_MAX else 0
                
        
        
        