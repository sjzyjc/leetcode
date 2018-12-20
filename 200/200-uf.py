class UnionFind:
    def __init__(self, grid):
        n = len(grid) * len(grid[0])
        self.parents = [i for i in range(n)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    self.parents[i * len(grid[0]) + j] = -1 
        
        self.sizes = [1 for _ in range(n)]
        
    def find(self, i , j):
        return self.root(i) == self.root(j)
    
    def union(self, i, j):
        i = self.root(i)
        j = self.root(j)
        
        if self.sizes[i] < self.sizes[j]:
            self.parents[i] = j
            self.sizes[j] += self.sizes[i]
        else:
            self.parents[j] = i
            self.sizes[i] += self.sizes[j]
            
    def root(self, i):
        if self.parents[i] == -1:
            return -1
        
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
            
        return i
        
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        uf = UnionFind(grid)
        offsets = [[1, 0], [0, 1]]
        width = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue
                
                for offset in offsets:
                    neighbor_i = i + offset[0]
                    neighbor_j = j + offset[1]
                    if not (0 <= neighbor_i < len(grid) and 0 <= neighbor_j < len(grid[i])):
                        continue
                    
                    if grid[neighbor_i][neighbor_j] == "1":
                        uf.union(width * i + j, width * neighbor_i + neighbor_j)
                        
        counter = 0
        root_set = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                root = uf.root(width * i + j)
                if root != -1:
                    root_set.add(root)
        
        return len(root_set)
        
                