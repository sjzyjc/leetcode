class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        
        arr = s[::-1].split(' ')
        ans = []
        for i in arr:
            if not i:
                continue
                
            ans.append(i[::-1])
            
        return ' '.join(ans)
            
    