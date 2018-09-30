class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0:
            return ""
        
        romanValues = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
        
        ans = []
        divident = 1000
        while num > 0:
            tmp = num // divident
            
            if tmp in [1, 4, 5, 9]:
                ans.append(romanValues[tmp * divident])
            else:
                if tmp > 5:
                    ans.append(romanValues[5 * divident])
                
                for i in range(tmp % 5):
                    ans.append(romanValues[1 * divident])
                
            num -= divident * tmp
            divident //= 10
            
        return "".join(ans)