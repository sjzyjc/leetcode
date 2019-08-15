from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strings:
            val = 0
            delta = ord(s[0]) - ord('a') 
            for charr in s:
                val = val * 26 + (ord(charr) - delta) % 26
                
            hash_map[val].append(s)
            
        return list(hash_map.values())
                
