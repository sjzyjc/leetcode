class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
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
    
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not edges and n > 1:
            return False
        
        uf = UnionFind(n)
        for v1, v2 in edges:
            if uf.find(v1, v2):
                return False
            
            uf.union(v1, v2)
        
        root_set = set()
        for v in range(n):
            root_set.add(uf.root(v))
            
        return len(root_set) == 1
        