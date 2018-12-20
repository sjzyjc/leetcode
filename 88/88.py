class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def merge(self, A, m, B, n):
        # write your code here
            
        ptr1, ptr2 = m-1, n-1
        next_pos = m + n - 1
        
        while ptr1 >= 0 and ptr2 >= 0:
            if A[ptr1] > B[ptr2]:
                A[next_pos] = A[ptr1]
                ptr1 -= 1
            else:
                A[next_pos] = B[ptr2]
                ptr2 -= 1
            
            next_pos -= 1

        while ptr2 >= 0:
            A[next_pos] = B[ptr2]
            ptr2 -= 1
            next_pos -= 1
            
        