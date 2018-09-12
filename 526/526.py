class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        arr = [i for i in range(1, N+1)]
        self.counter = 0

        self.permute(arr, 0)
        return self.counter
    
    def permute(self, arr, length):
        if length == len(arr):
            self.counter += 1
            
        for i in range(length, len(arr)):
            arr[length], arr[i] = arr[i], arr[length]
            if (arr[length] % (length+1) == 0 or (length+1) % arr[length] == 0) :
                self.permute(arr, length + 1)
            arr[length], arr[i] = arr[i], arr[length]
    
            