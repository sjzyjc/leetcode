class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        
        if len(A) == 1:
            return 1
        
        ans = 0
        tmp = 0
        for index, num in enumerate(A):
            if index == 0:
                tmp += 1
                
            elif 0 < index < len(A) - 1 and ((num > A[index - 1] and num > A[index + 1]) or ((num < A[index - 1] and num < A[index + 1]))):
                tmp += 1
            else:
                ans = max(ans, tmp + 1)
                tmp = 1
                
        return ans
                
                