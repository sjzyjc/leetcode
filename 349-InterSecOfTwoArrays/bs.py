class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        T: NlogN S: 1
        """
        result = set()
        for n in nums1:
            if self.binarySearch(sorted(nums2), n) != -1:
                result.add(n)

        return list(result) 

    def binarySearch(self, nums, n):
        start, end = 0, len(nums)-1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == n:
                return mid
            elif nums[mid] < n:
                start = mid + 1
            else:
                end = mid - 1    

        return -1