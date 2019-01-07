class UnionFind:
    def __init__(self, n):
        self.parents = [0 for _ in range(n)]
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

            

