class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = s.split(' ')
        
        ans = []
        for str in str_list:
            ans.append(str[::-1])
        
        return " ".join(ans)