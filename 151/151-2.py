class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        
        arr = list(s)
        self.reverse(arr, 0, len(arr) - 1)
        #print('!' + ''.join(arr) + '!')
        arr = self.trim(arr)
        #print('!' + ''.join(arr) + '!')        
        self.reverseWord(arr)
        return ''.join(arr)
    
    def reverse(self, arr, left, right):
        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    def trim(self, arr):
        left = right = 0
        while right < len(arr):
            if arr[right] == ' ' and (right == 0 or arr[right - 1] == ' '):
                right += 1
            else:
                arr[left] = arr[right]
                left += 1
                right += 1
                
        if left == 0:
            return []
        return arr[:left] if arr[left - 1] != ' ' else arr[:left - 1]
                
                  
    def reverseWord(self, arr):
        left = 0
        right = 0
        while right < len(arr) + 1:
            if right == len(arr) or arr[right] == ' ':
                self.reverse(arr, left, right - 1)
                left = right + 1
            
            right += 1
                
        
                
                
        
            
    