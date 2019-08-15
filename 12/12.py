romanValues = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0:
            return ""
        
        divisor = 1000
        ans = ''
        
        while num > 0:
            count = num // divisor
            if count in [4, 5, 9]:
                ans += romanValues[divisor * count]
            elif count < 4:
                ans += count * romanValues[divisor]
            elif count > 5:
                ans += romanValues[5 * divisor] + (count - 5) * romanValues[divisor]
                
            num -= count * divisor
            divisor //= 10
            
        return ans
            
                