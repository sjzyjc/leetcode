class Solution:
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) <= 1:
            return False
        
        memo = {}
        s = list(s)
        return self.helper(s, memo)
    
    def helper(self, s, memo):
        strr = "".join(s)
        if strr in memo:
            return memo[strr]
        
        ans = False
        for k in range(len(s) - 1):
            if s[k] == '+' and s[k] == s[k + 1]:
                #flip k and k + 1
                s[k] = '-'
                s[k + 1] = '-'
                     
                if self.helper(s, memo) is False:
                    s[k] = '+'
                    s[k + 1] = '+'
                    ans = True
                    break
                
                s[k] = '+'
                s[k + 1] = '+'
        
       
        #print("return F", s)
        memo[strr] = ans
        return ans
                