class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.ans = 0
        pair = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        for i in range(len(low), len(high) + 1):
            self.permute(0, i - 1, low, high, [None for _ in range(i)], pair)
            
        return self.ans
    
    def permute(self, start, end, low, high, carry, pair):
        if start > end:
            tmp = "".join(carry)
            if len(tmp) == len(low) and int(tmp) < int(low):
                return
            
            if len(tmp) == len(high) and int(tmp) > int(high):
                return
            
            self.ans += 1
            return
        
        for item in pair:
            if start == end and item in ["6", "9"]:
                continue
                
            if end != 0 and start == 0 and item == "0":
                continue
                
            carry[start] = item
            carry[end] = pair[item]
            self.permute(start + 1, end - 1, low, high, carry, pair)
                