import heapq
from collections import defaultdict
class Solution:
    def leastInterval(self, tasks, n):
        if not tasks:
            return 0
        
        if not n or n < 0:
            return len(tasks)
        
        
        count_map = defaultdict(int)
        for task in tasks:
            count_map[task] += 1
        
        heap = []
        for i in count_map:
            heapq.heappush(heap, -count_map[i])
            
        time = 0
        count = 0
        while heap:
            print(heap, time)
            tmp = []
            while count < n + 1:
                print(count)
                count += 1
                time += 1
                
                count = -heapq.heappop(heap) if heap else 1
                if count > 1:
                    tmp.append(count - 1)
                
                if not heap and not tmp:
                    return time
                
            count = 0
            for item in tmp:
                heapq.heappush(heap, -item)


sl = Solution()
print(sl.leastInterval(["A", "A", "A", "B", "B"], 2))