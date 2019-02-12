import heapq
class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or not k:
            return -1
        
        nums.sort()
        heap = []
        for index in range(len(nums)):
            if index + 1 < len(nums):
                heapq.heappush(heap, (nums[index + 1] - nums[index], index, index + 1))
        
        ans = -1
        for _ in range(k):
            ans, i, j = heapq.heappop(heap)
            
            j += 1
            if j < len(nums):
                heapq.heappush(heap, (nums[j] - nums[i], i, j))
        
        return ans
            
        
        