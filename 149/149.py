# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

from fractions import gcd
from collections import defaultdict
class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        
        if len(points) <= 2:
            return len(points)

        ans = 0
        for i in range(1, len(points)):
            hash_map = defaultdict(int)
            same_point = 1
            for j in range(i):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    same_point += 1
                
                else:
                    self.compute(i, j, points, hash_map)
                
            tmp = 0
            for item in hash_map:
                tmp = max(tmp, hash_map[item])
            ans = max(ans, tmp + same_point)
                

        return ans
    
    def compute(self, i, j, points, hash_map):
        x1, y1 = points[i].x, points[i].y
        x2, y2 = points[j].x, points[j].y
        
        if x1 != x2:
            para = gcd(y1 - y2, x1 - x2)
            divident, divisor = (y1 - y2) / para, (x1 - x2) / para
            hash_map[(divident, divisor)] += 1
        else:
            hash_map['INF'] += 1
        
            
            
            
            