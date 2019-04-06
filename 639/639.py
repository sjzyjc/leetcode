MOD  = 10 ** 9 + 7
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        one, two = 1, 0
        for i in range(1, len(s) + 1):
            cur = 0
            char = s[i - 1]
            if char == '*':
                cur = one * 9 
                if i > 1:
                    if s[i - 2] == '*':
                        cur += 15 * two
                    if s[i - 2] == '2':
                        cur += 6 * two
                    if s[i - 2] == '1':
                        cur += 9 * two
            else:
                if char != '0':
                    cur += one
                    
                if i > 1:
                    prev_char = s[i - 2]
                    if prev_char == '*':
                        if char <= '6':
                            cur += 2 * two
                        else:
                            cur += two
                    elif (prev_char == '1' or (prev_char == '2' and char <= '6')):
                        cur += two
                        
            cur %= MOD
            two = one
            one = cur
                        
        return cur
                
        