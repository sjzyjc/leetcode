class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges or n <= 2:
            return [i for i in range(n)]
        
        graph = collections.defaultdict(set)
        count = [0 for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
            count[v1] += 1
            count[v2] += 1
        
        ans = []
        min_height = (1 << 31) - 1
        for i in range(n):
            if count[i] == 1:
                continue
            
            visited = set()
            queue = collections.deque([i])
            level = 0
            while queue:
                if level > min_height:
                    break
                    
                length = len(queue)
                for _ in range(length):
                    node = queue.popleft()
                    
                    visited.add(node)
                    for nei in graph[node]:
                        if nei in visited:
                            continue
                        
                        queue.append(nei)
                level += 1
            
            if level == min_height:
                ans.append(i)
            elif level < min_height:
                ans = [i]
                min_height = min(level, min_height)
            #print(i, level, min_height)
            #print(ans)
                
        return ans
                
            
        