class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        
        memo = [-1 for _ in range(len(s) + 1)]
        return self.helper(s, wordDict, len(s) - 1, memo)
    
    def helper(self, s, wordDict, index, memo):
        if index < 0:
            return True
        
        if memo[index + 1] != -1:
            return memo[index + 1]
        
        can_break = False
        for j in range(0, index + 1):
            if s[j: index + 1] in wordDict and self.helper(s, wordDict, j - 1, memo):
                can_break = True
                break
                
        memo[index + 1] = can_break
        return can_break
                
                
                
            
        