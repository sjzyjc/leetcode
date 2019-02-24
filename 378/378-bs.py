class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        T: MN * log(max - min) //at most 32
        """

        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = (lo + hi)//2
            total = 0
            for i in range(len(matrix)):
                j = len(matrix[i]) - 1
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                
                total += j + 1
                
            if total < k:
                lo = mid + 1
            else:
                hi = mid
        return lo