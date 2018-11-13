class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return [[]]
        
        ans = collections.defaultdict(list)
        for strr in strs:
            count = [0 for i in range(26)]
            for char in strr:
                count[ord(char) - ord('a')] += 1
            
            ans[tuple(count)].append(strr)
            
        return list(ans.values())
            
        