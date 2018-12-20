class Solution:
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) <= 1:
            return False
        
        s = list(s)
        return self.helper(s)
    
    def helper(self, s):
        #print(s)
        for k in range(len(s) - 1):
            if s[k] == '+' and s[k] == s[k + 1]:
                #flip k and k + 1
                s[k] = '-'
                s[k + 1] = '-'
                     
                if self.helper(s) is False:
                    s[k] = '+'
                    s[k + 1] = '+'
                    return True
                
                s[k] = '+'
                s[k + 1] = '+'
        
       
        #print("return F", s)
        return False
                