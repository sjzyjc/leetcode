class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0]:
            return []
                
        for i in range(len(A)):
            ptr1, ptr2 = 0, len(A[i]) - 1
            while ptr1 <= ptr2:
                A[i][ptr1], A[i][ptr2] = 1 - A[i][ptr2], 1 - A[i][ptr1]
                ptr1 += 1
                ptr2 -= 1
                
        return A