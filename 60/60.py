import math
class Solution:
    def getPermutation(self, n, k):
        numbers = [i for i in range(1, n + 1)]
        permutation = ''
        k -= 1
        
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            numbers.remove(numbers[index])

        return permutation
            