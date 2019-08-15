BASE = 31
MOD = 10 ** 6
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #print(len(haystack))
        #print(len(needle))
        if haystack is None or needle is None or len(needle) > len(haystack):
            return -1
        
        if len(needle) == 0:
            return 0
        
        def gethash(s):
            val = 0
            for charr in s:
                val = (val * 31 + (ord(charr) - ord('a'))) % MOD
            
            return val
        
        target = gethash(needle)
        first = gethash(haystack[:len(needle)])
        
        if first == target:
            return 0
        
        l = len(needle)
        for i in range(l, len(haystack)):
            first = (first * 31 % MOD + ord(haystack[i]) - ord('a')) % MOD - ((ord(haystack[i - l]) - ord('a')) * (31 ** l) % MOD)
            first %= MOD
            
            if first == target and haystack[i - l + 1:i+1] == needle:
                return i - l + 1
            
            
        return -1
            
            
                
                
                
                
        return -1