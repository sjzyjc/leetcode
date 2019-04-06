class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s: s = ''
        if not t: t = ''
            
        if abs(len(s) - len(t)) >= 2:
            return False
        
        if len(s) == len(t) and self.checkModify(s, t):
            return True
        
        if len(s) > len(t) and self.checkAddRemove(s, t):
            return True
        
        if len(s) < len(t) and self.checkAddRemove(t, s):
            return True
        
        return False
    
    def checkModify(self, s, t):
        one_diff = False
        ptr = 0
        while ptr < len(s):
            if s[ptr] != t[ptr]:
                if one_diff:
                    return False
                
                one_diff = True
                
            ptr += 1
        
        return one_diff
    
    def checkAddRemove(self, long, short):
        extra_found = False
        ptr = 0
        while ptr < len(short):
            if extra_found:
                if long[ptr] != short[ptr - 1]:
                    return False
                
            else:
                if long[ptr] != short[ptr]:
                    extra_found = True
                    
            ptr += 1
            
        return long[ptr] == short[ptr - 1] if extra_found else True
        
        