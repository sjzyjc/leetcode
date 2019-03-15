UNIT = ["Billion", "Million", "Thousand"]
ONES = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
TWOS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'
        
        arr = [0 for _ in range(4)]
        index = 0
        divisor = 1000000000
        while index < 4:
            arr[index] = num // divisor
            num -= arr[index] * divisor
            divisor //= 1000
            index += 1
            
        ans = []
        for index in range(3):
            val = arr[index]
            if val == 0:
                continue
            
            ans.extend(self.helper(val))
            ans.append(UNIT[index])
            
        ans.extend(self.helper(arr[-1]))
        #print(ans)
        return " ".join(ans)
    
    def helper(self, val):
        arr = [0 for _ in range(3)]
        
        divisor = 100
        for index in range(3):
            arr[index] = val // divisor
            val -= arr[index] * divisor
            divisor //= 10
            
        ans = []
        if arr[0] != 0:
            ans.append(ONES[arr[0] - 1])
            ans.append("Hundred")
            
        if arr[1] == 1:
            ans.append(TWOS[arr[2]])
        else:
            if arr[1] != 0:
                ans.append(TENS[arr[1] - 2])
            
            if arr[2] != 0:
                ans.append(ONES[arr[2] - 1])
            
        return ans
        
            
            
            
            
    
        
        
        