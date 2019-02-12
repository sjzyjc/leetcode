class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if not nums or k <= 0:
            return []
        
        min_heap = []
        max_heap = []
        ans = []
        for index in range(len(nums)):
            num = nums[index]
            if not min_heap or num >= min_heap[0]:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappush(max_heap, -num)
                
            if index - k >= 0:
                to_remove = nums[index - k]
                if to_remove >= min_heap[0]:
                    min_heap.remove(to_remove)
                    heapq.heapify(min_heap)
                else:
                    max_heap.remove(-to_remove)
                    heapq.heapify(max_heap)
                    
            self.balance(min_heap, max_heap)
            if index >= k - 1:
                if k % 2 == 0:
                    ans.append((-max_heap[0] + min_heap[0]) / 2)
                else:
                    ans.append(min_heap[0] / 1)
            #print(index, ans)
                    
        return ans
        
    def balance(self, min_heap, max_heap):
        while len(max_heap) > len(min_heap):
            item = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -item)
            
        while len(min_heap) > len(max_heap) + 1:
            item = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -item)
            
            
            