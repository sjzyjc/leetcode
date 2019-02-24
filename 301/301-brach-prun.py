class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        
        ans = []
        self.helper(s, 0, -1, ans, ['(', ')'], [])
        
        ret = []
        print(ans)
        for item in ans:
            tmp = ""
            for j in range(len(s)):
                if j not in item: 
                    tmp += s[j]
                    
            ret.append(tmp)
                
        return ret
    
    def helper(self, s, start_index, last_remove, ans, pair, carry):        
        unmatched = 0
        i = start_index
        while i < len(s):
            char = s[i]
            if char == pair[0]: 
                unmatched += 1
            elif char == pair[1]:
                unmatched -= 1
            
            print(i, unmatched)
            if unmatched < 0:
                for j in range(last_remove + 1, i + 1):
                    if s[j] != pair[1]:
                        continue
                    
                    if s[j] == s[j - 1] and j - 1 > last_remove:
                        continue
                    
                    if pair[0] == '(':
                        carry.append(j)
                    else:
                        carry.append(len(s) - 1 - j)
                        
                    self.helper(s, i + 1, j, ans, pair, carry)
                    carry.pop()
                break
            i += 1
                  
        
        if i == len(s):
            if pair[0] == '(':
                self.helper(s[::-1], 0, -1, ans, pair[::-1], carry)
            else:
                ans.append(carry + [])
        

