
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        left = right = 0
        ans = 0
        
        for charr in s:
            if charr == '(':
                left += 1
            else:
                right += 1
                if right > left:
                    left = 0
                    right = 0
                    
                elif right == left:
                    ans = max(ans, right * 2)
                    
        left = right = 0
        for charr in s[::-1]:
            if charr == ')':
                right += 1
            else:
                left += 1
                if left > right:
                    left = 0
                    right = 0
                elif right == left:
                    ans = max(ans, right * 2)
                    
        return ans
                