class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key = lambda x: x[0])
        
        min_right = points[0][1]
        ans = 1 
        
        for index in range(1, len(points)):
            if points[index][0] <= min_right:
                min_right = min(min_right, points[index][1])
                continue
                
            min_right = points[index][1]
            ans += 1
        
        return ans
            