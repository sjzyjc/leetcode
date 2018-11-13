class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        if not A or not B:
            return []
        
        hash_table = {}
        for index, item in enumerate(B):
            hash_table[item] = index
        
        ans = []
        for item in A:
            ans.append(hash_table[item])
            
        return ans