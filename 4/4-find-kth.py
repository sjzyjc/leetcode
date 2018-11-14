class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if nums1 is None:
            nums1 = []
            
        if nums2 is None:
            nums2 = []
            
        total_len = len(nums1) + len(nums2)
        
        if total_len % 2 == 0:
            return (self.findkth(nums1, nums2, 0, 0, total_len // 2) + self.findkth(nums1, nums2, 0, 0, total_len // 2 + 1)) / 2
        else:
            return self.findkth(nums1, nums2, 0, 0, total_len // 2 + 1)
        
    def findkth(self, nums1, nums2, i, j, k):
        if i >= len(nums1):
            return nums2[j + k - 1]
        
        if j >= len(nums2):
            return nums1[i + k - 1]
        
        if k == 1:
            return min(nums1[i], nums2[j])
        
        nums1_half = nums1[i + k // 2 - 1] if i + k // 2 - 1 < len(nums1) else (1 << 31) - 1
        nums2_half = nums2[j + k // 2 - 1] if j + k // 2 - 1 < len(nums2) else (1 << 31) - 1
        
        if nums1_half < nums2_half:
            return self.findkth(nums1, nums2, i + k // 2, j, k - k // 2)
        else:
            return self.findkth(nums1, nums2, i, j + k // 2, k - k // 2)