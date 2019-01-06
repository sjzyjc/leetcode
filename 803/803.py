class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.sizes = [1 for _ in range(n + 1)]
        
    def union(self, i, j):
        if self.find(i, j):
            return
        
        i = self.root(i)
        j = self.root(j)
        
        if self.sizes[i] < self.sizes[j]:
            self.parents[i] = j
            self.sizes[j] += self.sizes[i]
        else:
            self.parents[j] = i
            self.sizes[i] += self.sizes[j]
        
    
    def find(self, i, j):
        return self.root(i) == self.root(j)
    
    def root(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
            
        return i
        
        
class Solution:
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        if not hits or not grid:
            return [0]
        
        not_work = set()
        for i, j in hits:
            if grid[i][j] == 0:
                not_work.add((i, j))
            
            grid[i][j] = 0
        
        height = len(grid)
        width = len(grid[0])
        uf = UnionFind(width * len(grid))
        dummy = width * height
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    continue
                
                if i == 0:
                    uf.union(j, dummy)
                
                right = i * width + j + 1
                down = (i + 1) * width + j
                
                if j + 1 < width and grid[i][j + 1] == 1:
                    uf.union(i * width + j, right)
                    
                if i + 1 < height and grid[i + 1][j] == 1:
                    uf.union(i * width + j, down)
        
        
        size = uf.sizes[uf.root(dummy)]            
        ans = []
        for i, j in hits[::-1]:
            if (i, j) in not_work:
                ans.append(0)
                continue
                
            grid[i][j] = 1
            
            if i == 0:
                uf.union(j, dummy)
                
            offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for offset in offsets:
                new_i = i + offset[0]
                new_j = j + offset[1]
                
                if not (0 <= new_i < height and 0 <= new_j < width):
                    continue
                    
                if grid[new_i][new_j] == 0:
                    continue
                    
                uf.union(new_i * width + new_j, i * width + j)
            
            new_size = uf.sizes[uf.root(dummy)]
            #print(size, new_size, uf.sizes)

            ans.append(max(new_size - size - 1, 0))
            size = new_size
            
        return ans[::-1]
                        
        
        