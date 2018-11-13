import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        count_map = {i:0 for i in nums}
        for num in nums:
            count_map[num] += 1
        
        heap = []
        ans = []
        for key in count_map:
            if len(heap) < k:
                heapq.heappush(heap, (count_map[key], key))
                continue
            
            if count_map[key] <= heap[0][0]:
                continue
                
            heapq.heappush(heap, (count_map[key], key))
            heapq.heappop(heap)
                
        for item in heap:
            ans.append(item[1])
        return ans