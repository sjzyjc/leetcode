class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr or k < 0:
            return []
        
        if k >= len(arr):
            return arr
        
        if x > arr[-1]:
            return arr[-k:]
        
        if x < arr[0]:
            return arr[:k]
        
        start, end = 0, len(arr) - 1
        
        # k must witin range arr, find first larger or equal
        while start < end:
            mid = start + (end - start) // 2
            
            if arr[mid] >= x:
                end = mid
            else:
                start = mid + 1
                
        if arr[start] != x:
            if abs(arr[start - 1] - x) < abs(arr[start] - x):
                start = start - 1
        
        left, right = max(0, start - k + 1), min(len(arr) - 1, start + k - 1)
        
        while right - left + 1 > k:
            if left < 0:
                return arr[:k]
                
            if right > len(arr) - 1:
                return arr[-k:]
                
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1  
            else:
                right -= 1
                
                            
        return arr[left:right + 1]
                
            
                