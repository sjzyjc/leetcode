class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        if not str:
            return
        
        self.reverse(str, 0, len(str) - 1)
        start, end = 0, 0
        
        while end < len(str):
            while end < len(str) and str[end] != " ":
                end += 1
                
            self.reverse(str, start, end - 1)
            start = end + 1
            end += 1

    def reverse(self, str, start, end):
        left, right = start, end
        while left < right:
            str[left], str[right] = str[right], str[left]
            left += 1
            right -= 1
            
        