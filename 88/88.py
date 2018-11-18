class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2 or m < 0 or n < 0:
            return 
        
        if nums2[0] >= nums1[m - 1]:
            nums1[m:] = nums2
            return
        
        if nums1[0] >= nums2[-1]:
            nums1[len(nums1) - m:] = nums1[:m]
            nums1[:n] = nums2
            return
            
        ptr1, ptr2 = m-1, n-1
        next_pos = len(nums1) - 1
        
        while next_pos >= 0:
            num1 = nums1[ptr1] if ptr1 >= 0 else -(1 << 31)
            num2 = nums2[ptr2] if ptr2 >= 0 else -(1 << 31)
            
            if num1 > num2:
                nums1[next_pos] = num1
                ptr1 -= 1   
            else:
                nums1[next_pos] = num2
                ptr2 -= 1
            next_pos -= 1
        
            
        
                