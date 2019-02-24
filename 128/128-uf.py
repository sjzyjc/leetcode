class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1 for _ in range(n)]
        
    def union(self, i, j):
        if self.find(i, j):
            return
        
        i = self.root(i)
        j = self.root(j)
        if self.sizes[i] > self.sizes[j]:
            self.parents[j] = i
            self.sizes[i] += self.sizes[j]
        else:
            self.parents[i] = j
            self.sizes[j] += self.sizes[i]
            
    def find(self, i, j):
        return self.root(i) == self.root(j)
    
    def root(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
            
        return i
    

class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        
        visited = {}
        uf = UnionFind(len(nums))
        for index, num in enumerate(nums):
            if num in visited:
                continue
            
            visited[num] = index
            if num + 1 in visited:
                uf.union(index, visited[num + 1])
                
            if num - 1 in visited:
                uf.union(index, visited[num - 1])
        
        ans = 1
        #print(uf.sizes)
        for index in range(len(nums)):
            ans = max(ans, uf.sizes[index])
        
        return ans
                
                
        
        