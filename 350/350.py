class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        O(MN)
        """
        if not nums1 or not nums2:
            return []
        
        ret = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ret.append(nums1[i])
                    nums1[i] = None
                    nums2[j] = None
                    break
        
        return ret