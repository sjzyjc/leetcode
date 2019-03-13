class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        
        stack = []
        ans = [0 for _ in range(len(T))]
        for index in range(len(T)):
            val = T[index] 
            while stack and T[stack[-1]] < val:
                j = stack.pop()
                ans[j] = index - j
                
            stack.append(index)
            
        return ans
        