class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1 for _ in range(n)]

    def find(self, i, j):
        return self.root(i) == self.root(j)

    def root(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return i
        
    def union(self, i, j):
        i = self.root(i)
        j = self.root(j)
        if self.sizes[j] > self.sizes[i]:
            self.parents[i] = j
            self.sizes[j] += self.sizes[i]
        else:
            self.parents[j] = i
            self.sizes[i] += self.sizes[j] 

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        
        uf = UnionFind(len(M))
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j] == 0:
                    continue
                
                if not uf.find(i,j):
                    uf.union(i, j)
        
        root_set = set()
        for i in range(len(M)):
            root_set.add(uf.root(i))
        
        return len(root_set)
        
        