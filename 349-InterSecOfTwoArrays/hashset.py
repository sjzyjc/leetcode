class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    O(M + N)
    O(min(M, N))
    
    """
    def intersection(self, nums1, nums2):
        # write your code here
        if not nums1 or not nums2:
            return []
        
        nums2 = set(nums2)   
        ans = set()
        for num in nums1:
            if num in nums2:
                ans.add(num)
                
        return list(ans)