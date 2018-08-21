class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        tmp = self.trie

        for charr in word:
            if charr not in tmp:
                tmp[charr] = {}
            tmp = tmp[charr]

        tmp['#'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.startsWith(word+'#')

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tmp = self.trie
        for charr in prefix:
            if charr not in tmp:
                return False
            tmp = tmp[charr]

        return True



# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("abc")
obj.insert("abd")
print(obj.trie)
print(obj.startsWith("ab"))
print(obj.startsWith("ac"))
print(obj.search("abc"))
print(obj.search("abe"))
