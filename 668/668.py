import heapq
class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        klogk good when k is small
        """
        if not m or not n or not k:
            return 0
        
        if m < 0 or n < 0:
            return 0
        
        heap = []
        heapq.heappush(heap, (1, 1, 1))
        visited = set()
        visited.add((1, 1))
        
        ans = 0
        for _ in range(k):
            ans, i, j = heapq.heappop(heap)
            if i + 1 <= m and (i+1, j) not in visited:
                heapq.heappush(heap, ((i + 1) * j, i + 1,  j))
                visited.add((i + 1, j))
                
            if j + 1 <= n and (i, j + 1) not in visited:
                heapq.heappush(heap, (i * (j + 1), i, j + 1))
                visited.add((i, j + 1))
                
        return ans

sl = Solution()
print(sl.findKthNumber(9895,28405,100787757))
                
            
            