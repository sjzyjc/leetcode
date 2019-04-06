from collections import defaultdict, deque
OFFSETS = [[0, 1], [1, 0]]
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        graph = defaultdict(set)
        in_degree = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for offset in OFFSETS:
                    new_i = i + offset[0]
                    new_j = j + offset[1]
                    
                    if not (0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0])):
                        continue
                        
                    if matrix[new_i][new_j] > matrix[i][j]:
                        graph[(i, j)].add((new_i, new_j))
                        in_degree[new_i][new_j] += 1
                        
                    
                    if matrix[i][j] > matrix[new_i][new_j]:
                        graph[(new_i, new_j)].add((i, j))
                        in_degree[i][j] += 1
                        
        #topo sort
        queue = deque([])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if in_degree[i][j] == 0:
                    queue.append((i, j))
        
        ans = 0
        while queue:
            l = len(queue)
            for _ in range(l):
                i, j = queue.popleft()
                
                for nei in graph[(i , j)]:
                    in_degree[nei[0]][nei[1]] -= 1
                    if in_degree[nei[0]][nei[1]]  == 0:
                        queue.append(nei)
                        
            ans += 1
            
        return ans
            
                        
        
        
                
        