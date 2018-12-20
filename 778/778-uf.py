class UnionFind:
    def __init__(self, grid):
        n = len(grid) * len(grid[0])
        self.parents = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]
        
    def find(self, i, j):
        return self.root(i) == self.root(j)
    
    def union(self, i, j):
        #print("union", i, j)
        i = self.root(i)
        j = self.root(j)
        
        if self.sizes[i] < self.sizes[j]:
            self.parents[i] = j
            self.sizes[j] += self.sizes[i]
            
        else:
            self.parents[j] = i
            self.sizes[i] += self.sizes[j]
            
    def root(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
            
        return i

class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        
        uf = UnionFind(grid)
        level = 0
        width = len(grid[0])
        index = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                index[grid[i][j]] = (i, j)
        
        
        while not uf.find(0, len(grid) * len(grid[0]) - 1):
            index_i, index_j = index[level]
            offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for offset_i, offset_j in offsets:
                if not (0 <= index_i + offset_i < len(grid) and 0 <= index_j + offset_j < len(grid[0])):
                    continue
                
                new_i = index_i + offset_i
                new_j = index_j + offset_j
                if grid[new_i][new_j] > level:
                    continue
                    
                uf.union(index_i * width + index_j, new_i * width + new_j)
                
            level += 1
            
        return level - 1
            
        