class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        
        self.ans = []
        self.permute(n * 2, 0, "")
        return self.ans
    
    def permute(self, n, length, strr):
        if length == n:
            self.ans.append(strr)
            return
        
        for i in ['(', ')']:
            strr = strr + i
            if strr.count('(') >= strr.count(')') and strr.count('(') <= (n // 2):
                self.permute(n, length + 1, strr)
            strr = strr[:-1]
                
        