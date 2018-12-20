class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not words:
            return -1
        
        last_word = -1
        ans = (1 << 31) - 1
        for index, word in enumerate(words):
            if word != word1 and word != word2:
                continue
            
            if last_word != -1 and word != words[last_word]:
                ans = min(ans, index - last_word)
                
            last_word = index
            
        return ans