# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        if not A or not B:
            return []
        
        #A.sort(key = lambda x: x.start)
        #B.sort(key = lambda x: x.start)
        
        i = 0
        j = 0
        ans = []
        #overrlap A.end >= B.start and A.start <= B.end
        while i < len(A) and j < len(B):
            if A[i].end < B[j].start:
                i += 1
            
            elif B[j].end < A[i].start:
                j += 1
                
            else:
                if i < len(A) and j < len(B):
                    ans.append([max(A[i].start, B[j].start), min(A[i].end, B[j].end)])
                
                if j + 1 == len(B) or (i + 1 < len(A) and A[i + 1].start < B[j + 1].start):
                    i += 1
                else:
                    j += 1
                    
        return ans
                    
                    
            