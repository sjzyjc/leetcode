from collections import defaultdict
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
            graph[depart].append(arrive)
            
        return self.dfs(graph, tickets, "JFK", ["JFK"])[0]
        
    
    def dfs(self, graph, tickets, current, carry):
        if len(tickets) == 0:
            return carry, True
        
        for nei in sorted(graph[current]):
            if [current, nei] not in tickets:
                continue
                
            carry.append(nei)
            tickets.remove([current, nei])
            if self.dfs(graph, tickets, nei, carry)[1]:
                return carry, True
            
            tickets.append([current, nei])
            carry.pop()
        return carry, False
        