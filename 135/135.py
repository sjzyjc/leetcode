from collections import defaultdict, deque
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        count = 0
        graph = defaultdict(set)
        in_degree = [0 for _ in range(len(ratings))]
        for index, rating in enumerate(ratings):
            if index >= 1 and rating < ratings[index - 1]:
                graph[index].add(index - 1)
                in_degree[index - 1] += 1
                    
            if index + 1 < len(ratings) and rating < ratings[index + 1]:
                graph[index].add(index + 1)
                in_degree[index + 1] += 1
                
        queue = deque([])
        for node in range(len(in_degree)):
            if in_degree[node] == 0:
                queue.append((node, 1))
        
        #print(graph, in_degree)
        ans = 0
        while queue:
            node, candy = queue.popleft()
            ans += candy
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append((nei, candy + 1))
                    
        return ans
            
        
        