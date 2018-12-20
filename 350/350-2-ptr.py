class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        NlogN + MlogM + N + M where N = max(N, M)
        merge sorted list
        """
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        
        ret = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:    
                j += 1
            else:
                ret.append(nums1[i])
                i += 1                
                j += 1
                
        return ret