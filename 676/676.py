class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        if dict is None:
            return
        
        for word in dict:
            self.set.add(word)
            
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if word is None:
            return False
        
        for i in range(len(word)):
            prefix = ""
            if i > 0:
                prefix = word[:i]
            
            for j in range(26):
                if chr(ord('a') + j) == word[i]:
                    continue 
                    
                if prefix + chr(ord('a') + j) + word[i + 1:] in self.set:
                    return True
                
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)