class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        var_set = set()
        graph = collections.defaultdict(set)
        for index in range(len(equations)):
            divident, divisor = equations[index]
            result = values[index]
            
            graph[divident].add((divisor, result))
            graph[divisor].add((divident, 1 / result))
            var_set.add(divisor)
            var_set.add(divident)
            
        ans = []
        for divident, divisor in queries:
            if divisor not in var_set or divident not in var_set:
                ans.append(-1.0)
                continue
            
            visited = set()
            result = self.dfs(graph, divident, divisor, visited, 1)[0]
            ans.append(result)
            graph[divident],add(divisor)

        return ans
    
    def dfs(self, graph, cur, end, visited, carry):
        if cur == end:
            return carry, True
        
        visited.add(cur)
        for nei, weight in graph[cur]:
            if nei in visited:
                continue
            
            result, found = self.dfs(graph, nei, end, visited, carry * weight)
            if found:
                return result, True
        
        return -1.0, False