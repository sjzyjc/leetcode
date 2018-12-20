class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows <= 1:
            return s
        
        ans = ""
        for i in range(numRows):
            row = []
            j = i
            while j < len(s):
                row.append(s[j])
                if j + 2 * (numRows - i - 1) < len(s) and i != 0 and i != numRows - 1:
                    row.append(s[j + 2 * (numRows - i - 1)])
                
                j += 2 * numRows - 2
            
            #print(row)
            ans += "".join(row)
            
        return ans
                    
                
        