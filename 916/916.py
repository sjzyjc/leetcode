from collections import defaultdict
class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        if not B:
            return A
        
        if not A:
            return []
        
        counter_B = defaultdict(int)
        for word in B:
            tmp = defaultdict(int)
            for c in word:
                tmp[c] += 1
            
            for i in tmp:
                counter_B[i] = max(counter_B[i], tmp[i])
        ans = []
        for word in A:
            is_valid = True
            counter_A = defaultdict(int)
            for c in word:
                counter_A[c] += 1
            
            for i in counter_B:
                if counter_A[i] < counter_B[i]:
                    is_valid = False
                    break
            
            if is_valid:
                ans.append(word)
                
        return ans
                
            
            
            
                