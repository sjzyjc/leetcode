class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return None
            
        s = self.reverse(list(s))

        ptr = 0
        tmp = ""
        ans = ""
        while ptr < len(s):
            if len(tmp) > 0 and s[ptr] == " ":
                ans += " "
                ans += self.reverse(list(tmp))
                tmp = ""
            
            while ptr < len(s) and s[ptr] == " ":
                ptr += 1
            
            if ptr < len(s):
                tmp += s[ptr]
                if ptr == len(s) - 1:
                    ans += " "
                    ans += self.reverse(list(tmp))
                    
            ptr += 1
        
        return ans[1:]
        
        
    def reverse(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return "".join(arr)
        