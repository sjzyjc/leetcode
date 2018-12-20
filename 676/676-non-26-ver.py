"""
count regular expression of neigbor
buildDict: O(S) S: total chars
search: O(l) l:length of word
"""
from collections import defaultdict
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()
        self.close = defaultdict(int)
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        if not dict:
            return
        
        for word in dict:
            self.words.add(word)
            
            for index in range(len(word)):
                self.close[word[:index] + '*' + word[index + 1:]] += 1
                
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if word is None:
            return False
        
        for index in range(len(word)):
            if self.close[word[:index] + '*' + word[index + 1:]] == 1 and word not in self.words:
                return True
            
            if self.close[word[:index] + '*' + word[index + 1:]] > 1:
                return True
            
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)