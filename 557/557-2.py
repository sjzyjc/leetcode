class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        tmp = []
        ans = ""
        for index, charr in enumerate(s):
            if charr != ' ':
                tmp.append(charr)
                
            if charr == ' ':
                ans = ans + self.reverse(tmp) + " "
                tmp = []
                
        if len(tmp) != 0:
            ans += self.reverse(tmp)
            
        return ans
    
    def reverse(self, listt):
        left, right = 0, len(listt) - 1
        
        while left <= right:
            listt[left], listt[right] = listt[right], listt[left]
            left += 1
            right -= 1
            
        return "".join(listt)     
                
                
                
                
                