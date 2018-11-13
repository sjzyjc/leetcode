import heapq
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return -1
        
        queue = []
        heapq.heappush(queue, 1)
        visited = set()
        visited.add(1)
        
        for i in range(n):
            ans = heapq.heappop(queue)
            for multi in [2, 3, 5]:
                if ans * multi in visited:
                    continue
                
                visited.add(ans * multi)
                heapq.heappush(queue, ans * multi)
                
        return ans