class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if not letters or not target:
            return ""
        
        start, end = 0, len(letters) - 1
        if ord(target) >= ord(letters[end]):
            return letters[0]
        
        while start < end:
            mid = start + (end - start) // 2
            
            if ord(letters[mid]) > ord(target):
                end = mid
            else:
                start = mid + 1
        
        return letters[start]
        
        
        
        