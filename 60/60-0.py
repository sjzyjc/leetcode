import math
class Solution:

    def getPermutation(self, n, k):
        numbers = [i for i in range(1, n + 1)]
        k -= 1
        ans = ""
        
        divident = math.factorial(n - 1)
        offset = 1
        while offset <= n:
            index = k // divident
            k = k % divident
            
            if not numbers:
                break
                
            ans += str(numbers[index])
            numbers.remove(numbers[index])
            
            if offset < n:
                divident //= n - offset
                offset += 1
            

        return ans