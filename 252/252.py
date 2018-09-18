# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
        
        intervals.sort(key = lambda x: x.start)
        for index, interval in enumerate(intervals):
            if index == 0:
                continue
                
            if interval.start < intervals[index - 1].end:
                return False
        
        return True
            