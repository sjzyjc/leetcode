class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return [S]
        self.ans = []
        self.backtrack(S, 0)
        return self.ans

    def backtrack(self, S, index):
        if index == len(S):
            self.ans.append(S)
            return
        
        self.backtrack(S, index + 1)
        
        if S[index].isalpha():
            s_list = list(S)
            if s_list[index] == s_list[index].lower():
                s_list[index] = s_list[index].upper() 
            else:
                s_list[index] = s_list[index].lower()
            S = "".join(s_list)    
            self.backtrack(S, index + 1)
            
        
    

        
            
        