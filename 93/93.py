class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) > 12:
            return []
        
        ans = []
        self.helper(s, 0, ans, [], 4)
        return ans
    
    def helper(self, s, ptr, ans, carry, left):
        if (ptr == len(s) and left > 0) or (ptr < len(s) and left  == 0):
            return
        
        if ptr == len(s) and left == 0:
            ans.append('.'.join(carry + []))
            return
        
        for i in range(ptr + 1, len(s) + 1):
            sub_str = s[ptr: i]
            
            if not (0 <= int(sub_str) <= 255):
                break
            
            if sub_str[0] == '0' and len(sub_str) > 1:
                break
                
            carry.append(sub_str)
            self.helper(s, i, ans, carry, left - 1)
            carry.pop()
        
        