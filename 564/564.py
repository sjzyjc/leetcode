class Solution:
    def nearestPalindromic(self, S):
        if not S:
            return "1"
        
        if len(S) == 1:
            return str(int(S) - 1) if int(S) > 0 else "1"
        
        l = len(S)
        candidates = []
        candidates.append(str(10 ** l + 1))
        candidates.append(str(10 ** (l - 1) - 1))
        
        prefix = int(S[:(l - 1)//2 + 1])
        for start in [prefix - 1, prefix, prefix + 1]:
            if l % 2 == 0: #even
                candidates.append(str(start) + str(start)[::-1])
            else:
                candidates.append(str(start) + str(start)[::-1][1:])
        
        def delta(x):
            return abs(int(S) - int(x))
    
        ans = None
        for cand in candidates:
            if cand != S and not cand.startswith('0'):
                if not ans or delta(cand) < delta(ans) or (delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans