class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word, node):
        if not word:
            node['#'] = True
            return
        
        char = word[0]
        if char not in node:
            node[char] = {}
            
        if '.' not in node:
            node['.'] = {}
            
        self.insert(word[1:], node[char])
        self.insert(word[1:], node['.'])
            
            
    def search(self, word):
        tmp = self.trie
        for charr in word:
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
        self.trie.insert(word, self.trie.trie)
        #print(self.trie.trie)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.search(word + '#')
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)