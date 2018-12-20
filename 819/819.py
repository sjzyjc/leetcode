from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        if not paragraph:
            return ""
        
        hashset = set(banned)
        tmp = ""
        count = defaultdict(int)
        
        for strr in paragraph:
            if strr in [" ", "!", "?", "\'", ";", ".", ","]:
                if len(tmp) == 0:
                    continue
                    
                if tmp in hashset:
                    tmp = ""
                    continue
                
                count[tmp] += 1
                tmp = ""
            else:
                tmp += strr.lower()
                
        if len(tmp) != 0:
            count[tmp] += 1
        
        maxium = -1
        ans = ""
        for key, val in count.items():
            if val > maxium:
                maxium = val
                ans = key
            
        return ans
                