class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def findLengthOfLCIS(self, A):
        # write your code here
        if not A:
            return 0
            
        return self.find(A)

        
    def find(self, A):
        f = [1 for i in range(len(A))]
        maximum = 1
        
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                continue
            
            f[i] = f[i - 1] + 1
            if f[i] > maximum:
                maximum = f[i]
        
        return maximum