class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word):
        tmp = self.trie

        for char in word:
            if char not in parent:
                tmp[char] = {}

            tmp = tmp[char]
        tmp['#'] = True

    def startsWith(self, word):
        tmp = self.trie
        for char in word:
            if char not in tmp:
                return False

            tmp = tmp[char]

        return True    

    def search(self, word):
        return self.startsWith(word + '#')    
