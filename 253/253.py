# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#nlogn
#n
import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        tmp = []
        for interval in intervals:
            tmp.append([interval.start, interval.end])
            
        tmp.sort()
        heap = []
        
        for index, interval in enumerate(tmp):
            if index == 0:
                heapq.heappush(heap, interval[1])
                continue
                
            last = heap[0]
            if interval[0] >= last:
                heapq.heappop(heap)
            
            heapq.heappush(heap, interval[1])
            
        return len(heap)
                
            
                
            
            
    
            
        