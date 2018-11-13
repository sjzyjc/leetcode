# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        
        listt = []
        for interval in intervals:
            listt.append([interval.start, interval.end])
            
        listt.sort()
        min_start = listt[0][0]
        max_end = listt[0][1]
        ans = []
        for index, interval in enumerate(listt):                
            if interval[0] <= max_end:
                max_end = max(max_end, interval[1])
            else:
                ans.append([min_start, max_end])
                min_start = interval[0]
                max_end = interval[1]
                
        ans.append([min_start, max_end])
        
        return ans
                
                
        