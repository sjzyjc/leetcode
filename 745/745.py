WEIGHT = False
class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word, weight):
        tmp = self.trie
        for charr in word:
            if charr not in tmp:
                tmp[charr] = {}
    
            tmp = tmp[charr]
            tmp[WEIGHT] = weight
    
    def find(self, word):
        tmp = self.trie
        for charr in word:
            if charr not in tmp:
                return -1
            
            tmp = tmp[charr]
            
        return tmp[WEIGHT]
                
class WordFilter:
    def __init__(self, words):
        self.trie = Trie()
        
        for weight, word in enumerate(words):
            for i in range(len(word), -1, -1):
                suffix = word[i:] + '#'
                self.trie.insert(suffix+word, weight)
                

    def f(self, prefix, suffix):
        return self.trie.find(suffix + '#' + prefix)