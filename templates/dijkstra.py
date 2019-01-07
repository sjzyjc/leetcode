import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        if not times or not (1 <= K <= N):
            return -1
        
        graph = defaultdict(set)
        for time in times:
            graph[time[0]].add((time[1], time[2]))
            
        remaining = [(0, K)]
        visited = set()
        weight = [(1 << 31) - 1 for _ in range(N)]
        weight[K - 1] = 0
        while remaining:
            cur_weight, node = heapq.heappop(remaining)
            
            if node in visited:
                continue
            
            for nei in graph[node]:
                if nei[0] not in visited and cur_weight + nei[1] < weight[nei[0] - 1]:
                    weight[nei[0] - 1] = cur_weight + nei[1]
                    heapq.heappush(remaining, (weight[nei[0] - 1], nei[0]))
                    
            visited.add(node)
        
        ans = max(weight)
        return ans if ans < (1 << 31) -1 else -1
        
        