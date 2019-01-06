from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return []
        
        graph = defaultdict(list)
        for depart, arrive in tickets:
            heapq.heappush(graph[depart], arrive)

            
        stack = ["JFK"]
        ans = []
        while stack:
            node = stack[-1]
            if len(graph[node]) == 0:
                ans.append(node)
                stack.pop()
            else:
                next_node = heapq.heappop(graph[node])
                stack.append(next_node)
        
        return ans[::-1]