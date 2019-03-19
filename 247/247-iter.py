
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        
        maps={"0":"0","1":"1","6":"9","8":"8","9":"6"}
        center = ["0", "1", "8"] if n % 2 == 1 else [""]
        
        while center: 
            if len(center[0]) == n:
                break
            
            tmp = []
            for c in center:
                for item in maps:
                    if len(c) == n - 2 and item == '0':
                        continue
                        
                    tmp.append(item + c + maps[item])
                    
            center = tmp
            #print(center)
            
        return center
                    
            
                    
                    
                    
                        
                        
        
        
            