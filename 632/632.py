import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        heap = []
        high = - (1 << 31)
        for index, listt in enumerate(nums):
            if not listt:
                continue
                            
            heapq.heappush(heap, (listt[0], index, 0))
            if listt[0] > high:
                high = listt[0]
                
            
        low = heap[0][0]
        ans = high - low
        ans_h = high
        ans_l = low
        
        while heap:
            cur_min, list_i, index = heapq.heappop(heap)
            
            if index + 1 >= len(nums[list_i]):
                break
                
            next_val = nums[list_i][index + 1]
            heapq.heappush(heap, (next_val, list_i, index + 1))
            
            high = max(high, next_val)
            low = heap[0][0]
            if high - low < ans:
                ans = high - low
                ans_h = high
                ans_l = low
                      
        return [ans_l, ans_h]
                    