class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key = lambda x: x[1])
        
        right = points[0][1]
        ans = 1
        for index in range(1, len(points)):
            if points[index][0] <= right:
                continue
                
            right = points[index][1]
            ans += 1
        
        return ans
        