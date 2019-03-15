UNIT = ["Billion", "Million", "Thousand", ""]
ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'
        
        index = 0
        divisor = 1000000000
        ans = ""
        for i in range(4):
            cur = num // divisor
            num -= cur * divisor
            divisor //= 1000
            
            if cur != 0:
                ans += self.helper(cur).strip() + " " + UNIT[i] + " "
            
        return ans.strip()
    
    def helper(self, val):
        if val == 0:
            return ""
        
        if val < 20:
            return ONES[val]
        elif val < 100:
            return TENS[val // 10] + " " + ONES[val % 10]
        else:
            return ONES[val // 100] + " Hundred " + self.helper(val % 100)
                
            
            
            
            
    
        
        
        