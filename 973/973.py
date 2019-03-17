class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points or K <= 0:
            return []
        
        def distance(point):
            return point[0] * point[0] + point[1] * point[1]
        
        def quickSelect(start, end, index):
            if start >= end:
                return 
            
            
            pivot = distance(points[(start + end) // 2])
            left = start
            right = end
            while left <= right:
                while left <= right and distance(points[left]) < pivot:
                    left += 1
                    
                while left <= right and distance(points[right]) > pivot:
                    right -= 1
                    
                if left <= right:
                    points[left], points[right] = points[right], points[left]
                    left += 1
                    right -= 1
                    
            if index < right:
                quickSelect(start, right, index)
                
            if index >= left:
                quickSelect(left, end, index)
                
        
        quickSelect(0, len(points) - 1, K - 1)
        
        return points[:K]
                
            