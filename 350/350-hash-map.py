from collections import defaultdict
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        map1, map2 = defaultdict(int), defaultdict(int)
        
        for num in nums1:
            map1[num] += 1
        
        for num in nums2:
            map2[num] += 1
            
        ret = []
        for i in map1:
            if i in map2:
                ret.extend([i for j in range(min(map1[i], map2[i]))])

                
        return ret