class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False
        
        str_list = str.split(" ")
        if len(str_list) != len(pattern):
            return False
        
        hashmap = {}
        for index, strr in enumerate(str_list):
            strr = strr + '$'
            if pattern[index] not in hashmap and strr not in hashmap:
                hashmap[pattern[index]] = strr
                hashmap[strr] = pattern[index]
            else:
                
                if pattern[index] in hashmap and strr in hashmap and hashmap[strr] == pattern[index] and hashmap[pattern[index]] == strr:
                    continue
                else:
                    return False
        
        return True