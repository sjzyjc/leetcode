class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return True
        
        paired_map = {}
        paired_map = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        left = 0 
        right = len(num) - 1
        while left <= right:
            if num[left] not in paired_map or paired_map[num[left]] != num[right]:
                return False
            
            left += 1
            right -= 1
            
        return True