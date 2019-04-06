from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""
        
        cur_dict = set()
        for word in words:
            for char in word:
                cur_dict.add(char)
                
        
        prev = words[0]
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        for i in range(1, len(words)):
            cur = words[i]
            ptr = 0
            while ptr < len(prev) and ptr < len(cur):
                if prev[ptr] != cur[ptr]:
                    if cur[ptr] not in graph[prev[ptr]]:
                        graph[prev[ptr]].add(cur[ptr])
                        in_degree[cur[ptr]] += 1
                    break
                    
                ptr += 1
                
            prev = cur
                      
        #print(graph, in_degree)
        #topo sort
        queue = deque([])
        for char in cur_dict:
            if char not in in_degree:
                queue.append(char)
                
        ans = ""
        while queue:
            node = queue.popleft()
            ans += node
            
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    del in_degree[nei]
                    queue.append(nei)
        
        #if cycle
        if len(in_degree) > 0:
            return ""
        
        return ans
            
            
                
            
            
            
        