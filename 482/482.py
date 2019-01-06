class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if not S:
            return ""
        
        S = S.replace("-", "")
        index = len(S) - 1
        
        ans = []
        while index + 1 > 0:            
            ans.append(S[max(index - K + 1, 0): index + 1].upper())
            index -= K
            
        return "-".join(ans[::-1])
            
        