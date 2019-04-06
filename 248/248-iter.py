class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        maps={"0":"0","1":"1","6":"9","8":"8","9":"6"}
        l_low, l_high =len(low), len(high)
        if l_low > l_high or (l_low == l_high and low>high): return 0
        
        middles = ["","0","1","8"]
        count = 0
        
        while middles:
            tmp = []
            for middle in middles:
                if len(middle) < l_high or (len(middle) == l_high and middle <= high):
                    if len(middle) > l_low or (len(middle) == l_low and middle >= low):  
                        if len(middle) > 1 and middle[0]=="0":
                            pass
                        else:
                            count+=1
                    
                    if l_high - len(middle) >= 2:                
                        for key in maps:
                            tmp.append(key + middle + maps[key])
            middles = tmp
            
        return count