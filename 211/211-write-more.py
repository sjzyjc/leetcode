class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word):
        tmp = self.trie
        for charr in word:
            if charr not in tmp:
                tmp[charr] = {}
                
            tmp = tmp[charr]
            
        tmp['#'] = True
    
    def search(self, word, trie):
        tmp = trie
        for index, charr in enumerate(word):
            if charr == '.':
                for item in tmp:
                    if item == '#':
                        continue 
                        
                    if self.search(word[index + 1:], tmp[item]):
                        return True
                return False
            else:
                if charr not in tmp:
                    return False
                
                tmp = tmp[charr]
        
        return True
                
                
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.insert(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.search(word + '#', self.trie.trie)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)