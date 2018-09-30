class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        
        ans = []
        self.helper(s, [], 0, ans)
        return ans
    
    def helper(self, s, carry, start_index, ans):
        if start_index == len(s):
            ans.append(carry + [])
            return
        
        for i in range(start_index, len(s)):
            if self.isPalindrome(s[start_index: i + 1]):
                carry.append(s[start_index: i + 1])
                self.helper(s, carry, i + 1, ans)
                carry.pop()
            
    
    def isPalindrome(self, string):
        left, right = 0, len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
            