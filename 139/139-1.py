class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        
        f = [False for _ in range(len(s) + 1)]
        f[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(0, i + 1):
                if s[j:i] in wordDict and f[j]:
                    f[i] = True
                    break
        
        return f[-1]