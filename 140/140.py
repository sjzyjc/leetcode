class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s or not wordDict:
            return []
        
        
        memo = [-1 for _ in range(len(s) + 1)]
        memo[0] = [""] 
        
        return self.helper(s, wordDict, len(s) - 1, memo)
        
    
    def helper(self, s, wordDict, index, memo):      
        if memo[index + 1] != - 1:
            return memo[index + 1]
        
        ans = []
        for i in range(0, index + 1):
            if s[i: index + 1] not in wordDict:
                continue 
                
            sub_strs = self.helper(s, wordDict, i - 1, memo)
            for sub_str in sub_strs:                        
                ans.append((sub_str + " " + s[i: index + 1]).strip())
        
        memo[index + 1] = ans
        return ans