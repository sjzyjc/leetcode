from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if N <= 0 or not edges:
            return []
        
        root = None
        nei_map = defaultdict(set)
        
        for start, end in edges:
            nei_map[start].add(end)
            nei_map[end].add(start)
            
        size_map = {}
        _, base = self.calSum(0, 0, nei_map, size_map, 0)

        print(base, size_map)   
        ans = {}
        self.traverse(0, base, nei_map, size_map, ans)
        return ans
    
    def calSum(self, node, distance, nei_map, size_map, total):
        print(node, size_map)
        if node in size_map:
            return 0, 0
        
        total += distance
        
        size = 1
        size_map[node] = 1
        for nei in nei_map[node]:
            size += self.calSum(nei, distance + 1, nei_map, size_map, total)[0]
        
        size_map[node] = size
        return size, total
        
    def traverse(self, node, node_sum, nei_map, size_map, ans):
        if node in ans:
            return
        
        ans[node] = node_sum
        for nei in nei_map[node]:
            self.traverse(nei, node_sum + (N - size_map[nei]) - size_map[nei], nei_map, size_map, ans)
        
            
sl = Solution()
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
N = 6
print(sl.sumOfDistancesInTree(N, edges))