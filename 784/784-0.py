class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return [S]
        
        return self.helper(S, 0)
    
    def helper(self, S, index):
        if index > len(S) - 1:
            return []
       
        
        sub = self.helper(S, index + 1)
        ans = []
        if not S[index].isalpha():
            if len(sub) == 0:
                ans.append(S[index])
            for i in sub:
                ans.append(S[index] + i)
        else:
            if len(sub) == 0:
                ans.append(S[index].lower())
                ans.append(S[index].upper())
            for i in sub:
                ans.append(S[index].lower() + i)
                ans.append(S[index].upper() + i)
                
        return ans
        
            
        