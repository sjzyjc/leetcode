class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        
        ans = 0
        left, right = 0, 0
        hashset = set()
        
        #increase i little by little to the right pos
        while left < len(s) and right < len(s):
            if s[right] not in hashset:
                hashset.add(s[right])
                right += 1
                ans = max(ans, right - left)
            else:
                #find dup
                hashset.remove(s[left])
                left += 1
                
            #print(left, right)
                        
        return ans
                
            
            
                