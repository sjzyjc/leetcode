from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1) > len(s2):
            return False
        
        target_count = defaultdict(int)
        window_count = defaultdict(int)
        
        for charr in s1:
            target_count[charr] += 1
            
        ptr = 0
        satisfy = 0
        while ptr < len(s2):
            charr = s2[ptr]
            window_count[charr] += 1
            
            if charr in target_count:
                if window_count[charr] == target_count[charr]:
                    satisfy += 1
                elif window_count[charr] == target_count[charr] + 1:
                    satisfy -= 1
                
            if ptr < len(s1) - 1:
                ptr += 1
                continue
                
            if ptr > len(s1) - 1:
                remove = s2[ptr - len(s1)]   
                print(ptr, remove)
                window_count[remove] -= 1
                    
                if remove in target_count:
                    if window_count[remove] == target_count[remove]:
                        satisfy += 1
                    elif window_count[remove] == target_count[remove] - 1:
                        satisfy -= 1
                    
            #print(window_count, satisfy, ptr)
            if satisfy == len(target_count):
                return True
            
            ptr += 1
            
            
        return False
                    
                
            