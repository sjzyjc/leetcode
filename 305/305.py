class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1 for _ in range(n)]
        
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
        while i !=  self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
            
        return i
    
OFFSETS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if not m or not n or not positions:
            return [0]
        
        uf = UnionFind(len(positions))
        index_map = {}
        idx = 0
        count = 0
        
        ans = []
        for position in positions:
            x = position[0]
            y = position[1]
            
            if (x, y) in index_map:
                continue
            
            index_map[(x, y)] = idx 
            root = set()
            for offset in OFFSETS:
                new_x = x + offset[0]
                new_y = y + offset[1]
                if (new_x, new_y) in index_map:
                    root.add(uf.root(index_map[(new_x, new_y)]))
                    uf.union(idx, index_map[(new_x, new_y)])
                    
            count = count - len(root) + 1
            ans.append(count)
            idx += 1
            
        return ans