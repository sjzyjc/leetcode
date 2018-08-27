class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        T: n S: n
        """
        nums1Set = set(nums1)
        nums2Set = set(nums2) 

        ret = []
        for num in nums1Set:
            if num in nums2Set:
                ret.append(num)

        return ret         