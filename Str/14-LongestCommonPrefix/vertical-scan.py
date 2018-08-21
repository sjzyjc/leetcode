class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""

        def isPartOfPrefix(index, c):
            for strr in strs[1:]:
                if index > len(strr) - 1 or strr[index] != c:
                    return False
            return True    

        result = ''
        for i in range(len(strs[0])):
            if not isPartOfPrefix(i, strs[0][i]):
                break
            result += strs[0][i]

        return result

    """
    Approach 2: Emumerate/Vertical scanning
    """
    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""   

        for index, c in enumerate(strs[0]):
            for strr in strs[1:]:
                if index >= len(strr) or strr[index] != c:
                    return strs[0][:index]

        return strs[0]

sl = Solution()
print(sl.longestCommonPrefix2(["flower","flow","flight"]))       
print(sl.longestCommonPrefix2(["dog","racecar","car"]))              
print(sl.longestCommonPrefix2(["aaaaaa","a","aa"]))  