from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]
        
    def find(self, i, j):
        self.root(i) == self.root(j)
        
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
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        if not stones:
            return 0
        
        uf = UnionFind(20000)
        for x, y in stones:
            uf.union(x, 10000 + y)
            
        root_set = set()
        for x,y in stones:
            root_set.add(uf.root(x))
            
        return len(stones) - len(root_set)
            
        

        