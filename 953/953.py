from collections import defaultdict
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words or not order:
            return True
        
        index_map = defaultdict(int)
        for index, charr in enumerate(order):
            index_map[charr] = index
            
        prev = words[0]
        for i in range(1, len(words)):
            cur = words[i]
            ptr = 0
            
            while ptr < min(len(prev), len(cur)):
                if prev[ptr] != cur[ptr]:
                    if index_map[cur[ptr]] < index_map[prev[ptr]]:
                        return False
                    else:
                        break
                        
                ptr += 1
            
            #abcd, abc
            if ptr == len(cur) and len(cur) < len(prev):
                return False
            
            prev = cur
            
            
        return True
            
                
            
            