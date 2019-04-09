class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        visited = set()
        count = 0
        while n != 1 and n not in visited:
            visited.add(n)
            tmp = 0
            while n > 0:
                tmp += (n % 10) * (n % 10)
                n = n // 10
            
            n = tmp
            count += 1
            print(n, visited)
                        
        return n == 1
    