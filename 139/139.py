class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        
        if not wordDict:
            return False
        
        match = [False for i in range(len(s))]
        break_point = [len(s)]
        
        for i in range(len(s) - 1, -1, -1):
            for j in break_point:
                if s[i:j] in wordDict:
                    match[i] = True
                    break_point.append(i)
                    break
            
        return match[0]