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
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        
        return i
        
        
class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n is None or n <= 0:
            return 0
        
        if not edges or not edges[0]:
            return n
        
        uf = UnionFind(n)
        for start, end in edges:
            uf.union(start, end)
        
        root = set()
        for i in range(n):
            root.add(uf.root(i))
            
        return len(root)