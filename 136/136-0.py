class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        hashset = set()
        for num in nums:
            if num in hashset:
                hashset.remove(num)
            else:
                hashset.add(num)
                
        return hashset.pop()