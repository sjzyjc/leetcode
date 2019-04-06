# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        interval_arr = []
        for interval in intervals:
            interval_arr.append((interval.start, 1))
            interval_arr.append((interval.end, 0))
            
        interval_arr.sort()
        count = 0
        ans = 0
        for i in interval_arr:
            if i[1] == 1:
                count += 1
                
            else:
                count -= 1
            
            ans = max(ans, count)
            
        return ans
                
            
        