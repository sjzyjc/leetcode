class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1 is None:
            nums1 = []
            
        if nums2 is None:
            nums2 = []
        
        m = len(nums1)
        n = len(nums2)
        if m <= n:
            return self.helper(nums1, nums2, (m + n) % 2 == 0)
        else:
            return self.helper(nums2, nums1, (m + n) % 2 == 0)
        
    def helper(self, nums1, nums2, is_even):
        start, end = 0, len(nums1)
        while start <= end:
            mid = (start + end) // 2
            nums1_small = nums1[mid - 1] if mid - 1 >= 0 else -(1 << 31)
            nums1_large = nums1[mid] if mid < len(nums1) else (1 << 31) - 1
            nums2_small = nums2[(len(nums1) + len(nums2)) // 2 - mid  - 1] if (len(nums1) + len(nums2)) // 2 - mid  - 1 >= 0 else -(1 << 31)
            nums2_large = nums2[(len(nums1) + len(nums2)) // 2 - mid] if (len(nums1) + len(nums2)) // 2 - mid < len(nums2) else (1 << 31) - 1
            
            #print(nums1_small, nums1_large, nums2_small, nums2_large)
            if max(nums1_small, nums2_small) <= min(nums1_large, nums2_large):
                if is_even:
                    return (max(nums1_small, nums2_small) + min(nums1_large, nums2_large)) / 2
                else:
                    return min(nums1_large, nums2_large)

            elif nums1_small > nums2_large:
                end = mid - 1
            else:
                start = mid + 1

        
                
        
                
            
            
            
            