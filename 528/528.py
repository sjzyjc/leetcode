import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        tmp = [-1 for _ in range(len(w) + 1)]
        for index, val in enumerate(w):
            tmp[index + 1] = tmp[index] + val
            
        self.freq = tmp[1:]
        print(self.freq)
        

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(0, self.freq[-1])
        start = 0
        end = len(self.freq) - 1
        
        #find last small
        while start + 1 < end:
            mid = (start + end) // 2
            if self.freq[mid] < target:
                start = mid
            else:
                end = mid - 1
        
        if self.freq[end] < target:
            return end + 1
        
        if self.freq[start] < target:
            return start + 1
        
        return 0
                
        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()