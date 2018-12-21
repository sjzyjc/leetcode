class Solution:
    def networkDelayTime(self, times, N, K):
        if not times or not (1 <= K <= N):
            return -1
        
        graph = collections.defaultdict(set)
        for time in times:
            graph[time[0]].add((time[2], time[1]))
            
        time = [(1 << 31) -1 for _ in range(N)]
        self.dfs(graph, K, time, 0)
        
        ans = max(time)
        return ans if ans != (1 << 31) -1 else -1
    
    def dfs(self, graph, node, time, cur_time):
        if cur_time >= time[node - 1]:
            return
        
        time[node - 1] = cur_time
        for weight, nei in sorted(graph[node]):
            self.dfs(graph, nei, time, cur_time + weight)
        
        
        