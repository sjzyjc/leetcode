# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x.start)
        min_right = intervals[0].end
        
        remove_count = 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start >= min_right:
                min_right = interval.end
                continue
                
            min_right = min(min_right, interval.end)
            remove_count += 1
            
        return remove_count
        