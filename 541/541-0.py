class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        counter = 0
        offset = 0
        tmp = []
        ans = []
        while counter < len(s):
            if counter % (2 * k) == 0:
                offset = 0
                
            if offset < k:
                tmp.append(s[counter])
            
            if offset == k - 1:
                ans.extend(tmp[::-1])
                tmp = []
            elif offset > k - 1:
                ans.append(s[counter])
                
            counter += 1
            offset += 1
            
        if len(tmp) > 0:
            ans.extend(tmp[::-1])
            
        return "".join(ans)
                
                
                
            
            
                