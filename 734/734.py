from collections import defaultdict
class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
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
        
        hash_map = defaultdict(set)
        for pair in pairs:
            hash_map[pair[0]].add(pair[1])
            hash_map[pair[1]].add(pair[0])
            
        for index in range(len(words1)):
            word1 = words1[index]
            word2 = words2[index]
            if word1 == word2:
                continue
                
            if word1 in hash_map and word2 in hash_map[word1]:
                continue
                
            return False
        
        return True