# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        if intervals is None:
            intervals = []
        
        
        insert_pos = 0
        ans = []
        for interval in intervals:
            if interval.end < newInterval.start:
                ans.append(interval)
                insert_pos += 1
                
            elif interval.start > newInterval.end:
                ans.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
                
        ans.insert(insert_pos, newInterval)
        return ans
                
                
        