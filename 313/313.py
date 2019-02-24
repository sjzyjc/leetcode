import heapq
class Solution:
    def nthSuperUglyNumber(self, n: 'int', primes: 'List[int]') -> 'int':
        if not primes or n <= 0:
            return -1
        
        f = [-1 for _ in range(n)]
        heap = []
        f[0] = 1
        visited = set()
        visited.add(1)
        
        for num in primes:
            heapq.heappush(heap, (num, num, 0))
        
        i = 1
        while i < n:
            product, prime, f_index = heapq.heappop(heap)
            if product not in visited:
                f[i] = product
                i += 1
                
            visited.add(product)
            heapq.heappush(heap, (prime * f[f_index + 1], prime, f_index + 1))
            
        return f[-1]
            
            
        