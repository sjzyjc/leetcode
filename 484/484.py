class Solution:
    def findPermutation(self, s: str) -> List[int]:
        if not s:
            return []
        
        visited = [False for _ in range(len(s) + 1)]
        def helper(start_index, start_val, s, carry):
            if start_index == len(s):
                return carry
            
            #print(start_index, start_val, s[start_index], carry)
            if s[start_index] == 'I':
                for i in range(start_val + 1, len(visited) + 1):
                    if visited[i - 1]:
                        continue
                        
                    visited[i - 1] = True
                    carry.append(i)
                    res = helper(start_index + 1, i, s, carry)
                    if res:
                        return res
                    
                    carry.pop()
                    visited[i - 1] = False
            else:
                for i in range(1, start_val):
                    if visited[i - 1]:
                        continue
                        
                    visited[i - 1] = True
                    carry.append(i)
                    res = helper(start_index + 1, i, s, carry)
                    if res:
                        return res
                    
                    carry.pop()
                    visited[i - 1] = False
                    
            return ""
            
        for i in range(1, len(visited) + 1):
            carry = [i]
            visited[i - 1] = True
            res = helper(0, i, s, carry)
            if res: 
                return res
            
            carry.pop()
            visited[i - 1] = False
            
        return ""
            
                
                    
                    
        