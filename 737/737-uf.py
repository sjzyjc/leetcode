class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1 for _ in range(n)]
    
    def find(self, i, j):
        return self.root(i) == self.root(j)
    
    def union(self, i ,j):
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
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if not words1 and not words2:
            return True
        
        if not words1 or not words2 or len(words1) != len(words2):
            return False
        
        index = 0
        index_map = {}
        uf = UnionFind(2 * len(pairs))
        for word1, word2 in pairs:
            if word1 not in index_map:
                index_map[word1] = index
                index += 1
                
            if word2 not in index_map:
                index_map[word2] = index
                index += 1
            
            uf.union(index_map[word1], index_map[word2])
            
        for i in range(len(words1)):
            word1 = words1[i]
            word2 = words2[i]
            
            if word1 == word2:
                continue
                
            if word1 in index_map and word2 in index_map and uf.find(index_map[word1], index_map[word2]):
                continue
                
            return False
        
        return True 
        
        