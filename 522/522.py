from collections import defaultdict
class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        if not strs:
            return -1
        
        strs.sort(key = len, reverse = True)
        
        for i in range(len(strs)):
            isValid = True
            for j in range(len(strs)):
                if i == j:
                    continue
                    
                if self.subseq(strs[i], strs[j]):
                    isValid = False
                    break
                    
            if isValid:
                return len(strs[i])            

        return -1

        
    def subseq(self, w1, w2):
        #True iff word1 is a subsequence of word2.
        i = 0
        for c in w2:
            if i < len(w1) and w1[i] == c:
                i += 1
        return i == len(w1)
            