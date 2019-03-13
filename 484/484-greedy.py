class Solution:
    def findPermutation(self, s: str) -> List[int]:
        if not s:
            return []
        
        ans = [i for i in range(1, len(s) + 2)]
        
        D_count = 0
        for index, val in enumerate(s):
            if val == 'I':
                if D_count > 0:
                    self.swap(ans, D_count, index - 1)
                D_count = 0
            else:
                D_count += 1
        
        self.swap(ans, D_count, index)
        return ans
    
    def swap(self, ans, count, last_D):
        start = last_D - count + 1
        end = last_D + 1
        while start < end:
            ans[start], ans[end] = ans[end], ans[start]
            start += 1
            end -= 1
                             
            
            