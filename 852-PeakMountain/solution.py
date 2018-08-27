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

        while start < end:  #quit when only 1 left, <= will cause dead loop since end will not move to mid - 1
            mid = start + (end - start) // 2

            if A[mid] < A[mid + 1]:
                start = mid + 1
            else:
                end = mid          #finding the first one which is larger than the one after

        return start