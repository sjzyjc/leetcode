class Solution:
    def splitIntoFibonacci(self, s):
        """
        :type S: str
        :rtype: List[int]
        """
        if not s:
            return []
        
        carry = []
        self.helper(s, 0, carry)
        return carry
    
    def helper(self, s, start_index, carry):
        #print(carry)
        if start_index == len(s) and len(carry) > 2:
            return True
        
        min_len = 1
        max_len = len(s) - 2
        if len(carry) >= 2:
            min_len = max(len(str(carry[-1])), len(str(carry[-2])))
            max_len = min_len + 1
            
        for l in range(min_len, min(max_len + 1, len(s) + 1 - start_index)):
            #print(start_index, start_index + l, s[start_index : start_index + l])
            if s[start_index] == '0' and l > 1:
                break

            num = int(s[start_index : start_index + l])
            
            if num > (1 << 31) - 1:
                break
                
            #first two number
            if len(carry) < 2:
                carry.append(num)
                res = self.helper(s, start_index + l, carry)
                if res:
                    return True
                carry.pop()
                continue
            
            #choose 3rd number and so on
            target = carry[-1] + carry[-2]
            if num < target:
                continue
            elif num == target:
                carry.append(num)
                res = self.helper(s, start_index + l, carry)
                if res:
                    return True
                
                carry.pop()
            else:
                break
                
        return False

