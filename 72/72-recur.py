class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            word1 = ""
            
        if not word2:
            word2 = ""
            
        memo = {}
        return self.dfs(word1, word2, 0, 0, memo)
    
    def dfs(self, word1, word2, w1_index, w2_index, memo):
        #print(w1_index, w2_index)
        if w1_index == len(word1) and w2_index == len(word2):
            return 0
        
        if w1_index == len(word1):
            return len(word2) - w2_index
        
        if w2_index == len(word2):
            return len(word1) - w1_index
        
        if (w1_index, w2_index) in memo:
            return memo[(w1_index, w2_index)]
        
        ans = len(word1) + len(word2)
        if word1[w1_index] == word2[w2_index]:
            ans = min(ans, self.dfs(word1, word2, w1_index + 1, w2_index + 1, memo))
        else:
            ans = min(ans, self.dfs(word1, word2, w1_index + 1, w2_index + 1, memo) + 1, self.dfs(word1, word2, w1_index + 1, w2_index, memo) + 1, self.dfs(word1, word2, w1_index, w2_index + 1, memo) + 1)
            
        memo[(w1_index, w2_index)] = ans
        return ans
            