import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: 'int'):
        if num is None:
            return
        
        if len(self.min_heap) == 0 or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        self.balance()
        
    def balance(self):
        while len(self.max_heap) > len(self.min_heap):
            item = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -item)
            
        while len(self.min_heap) > len(self.max_heap) + 1:
            item = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -item)
            
        
    def findMedian(self):
        # print("----")
        # print(self.max_heap)
        # print(self.min_heap)
        if self.max_heap and len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0] / 1.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()