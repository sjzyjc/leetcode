class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.trie = {}
        for word in words:
            self.insert(word)


    def insert(self, word):
        tmp =  self.trie
        for charr in word:
            if charr not in tmp:
                tmp[charr] =         
    