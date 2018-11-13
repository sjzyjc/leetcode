from collections import deque
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        queue = deque()
        for num in nums:
            queue.append([num])
        
        while queue:
            ans = [] 
            length = len(queue)
            
            for i in range(length):
                carry = queue.popleft()
                ans.append(carry)
                
                for num in nums:
                    if num in carry:
                        continue
                    carry.append(num)
                    queue.append(carry + [])
                    carry.remove(num)
                    
        return ans