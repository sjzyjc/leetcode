from collections import deque
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        queue = deque()
        nums.sort()
        visited = [False for i in range(len(nums))]
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1] and not visited[index - 1]:
                continue
            visited[index] = True
            queue.append([[num], visited + []])
            visited[index] = False
            
        while queue:
            ans = []
            length = len(queue)
            for i in range(len(queue)):
                carry, visited = queue.popleft()
                ans.append(carry)
                
                for index, num in enumerate(nums):
                    if visited[index]:
                        continue
                        
                    if index > 0 and num == nums[index - 1] and not visited[index - 1]:
                        continue
                        
                    carry.append(num)
                    visited[index] = True
                    queue.append((carry + [], visited + []))
                    visited[index] = False
                    carry.pop()
                    
        return ans