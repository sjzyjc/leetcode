from collections import defaultdict
from heapq import heappush, heappop

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return buildings
        
        # Critical points where we use negative heights for building's left points
        points = []
        for l, r, h in buildings:
            points += [(l, -h), (r, h)]
            
        # will be sorted based on whether they are left or right points.
        points.sort()
        
        # Use a heap to store heights where the last height is 0 and other elements are negative
        result = []
        heap = [0]
        prev = heap[0]
				
        # Save the heights that will be removed later
        ignored = defaultdict(int)
        
        for x, h in points:
            if h < 0:
                heappush(heap, h)
            else:
                ignored[-h] += 1

            #lazy remove
            while ignored[heap[0]] > 0:
                ignored[heap[0]] -= 1
                heappop(heap)

            # The first element is value of the heap's root node                
            cur = heap[0]
            if cur != prev:
                result.append((x, -cur))
                prev = cur
        
        return result