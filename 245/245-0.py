class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not words:
            return -1
        
        last_word1 = last_word2 = -(1 << 31)
        ans = (1 << 31) - 1
        for index, word in enumerate(words):
            if word != word1 and word != word2:
                continue
            
            if word1 == word2:
                ans = min(ans, index - last_word1)
                
            if word == word1:
                last_word1 = index
            
            if word == word2:
                last_word2 = index
            
            if word1 != word2:
                ans = min(ans, abs(last_word1 - last_word2))
            
        return ans