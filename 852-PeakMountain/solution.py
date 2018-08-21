class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A is None or len(A) == 0:
            return -1

        start = 0
        end = len(A) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if A[mid] < A[mid + 1]:
                return mid
            elif A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1  

        return -1