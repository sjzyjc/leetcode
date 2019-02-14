from collections import defaultdict
class Solution:
    def generatePalindromes(self, s: 'str') -> 'List[str]':
        if not s:
            return []
        
        count = defaultdict(int)
        for char in s:
            count[char] += 1
            
        odd = 0
        center = ""
        used = 0
        for key in count:
            if count[key] % 2 == 1:
                odd += 1
                center = key
                count[key] -= 1
                if count[key] == 0:
                    used += 1
                
            count[key] //= 2
                
        if odd > 1:
            return []
        
        ans = []
        self.permute(count, used, center, [], ans)
        return ans
    
    def permute(self, count, used, center, carry, ans):
        if used == len(count):
            substr = "".join(carry[::-1]) + center + "".join(carry)
            ans.append(substr)
            return
            
        for item in count:
            if count[item] == 0:
                continue
                
            count[item] -= 1
            if count[item] == 0:
                used += 1
                
            carry.append(item)
            self.permute(count, used, center, carry, ans)
            carry.pop()
            if count[item] == 0:
                used -= 1
            count[item] += 1
                
            
            
    

                
        