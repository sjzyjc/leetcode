class UnionFind:
    def __init__(self, n):
        self.parents = [-1 for _ in range(n)]
        self.sizes = [1 for _ in range(n)]
        
    def find(self, i, j):
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
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
            
        return i
    
    def updateParents(self, i):
        self.parents[i] = i
        
    def isValid(self, i):
        return self.parents[i] != -1
    
    
class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if not positions or m <= 0 or n <= 0:
            return []
        
        uf = UnionFind(m * n)
        offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ans = []
        for pos in positions:
            cur_index = pos[0] * n + pos[1]
            uf.updateParents(cur_index)
            
            new_islands = []
            prev_roots = set()
            for offset in offsets:
                new_pos_x, new_pos_y = pos[0] + offset[0], pos[1] + offset[1]
                if not (0 <= new_pos_x < m and 0 <= new_pos_y < n):
                    continue
                    
                new_index = new_pos_x * n + new_pos_y
                if not uf.isValid(new_index):
                    continue
                
                new_islands.append(new_index)
                prev_roots.add(uf.root(new_index))
                #uf.union(cur_index, new_index)
            
            for new_index in new_islands:
                uf.union(cur_index, new_index)
            
            new_roots = set()
            new_roots.add(uf.root(cur_index))
            for new_index in new_islands:
                new_roots.add(uf.root(new_index))

            if len(ans) == 0:
                ans.append(1)
            else:
                ans.append(ans[-1] + len(new_roots) - len(prev_roots))
            
        return ans
                
            
        
        
        