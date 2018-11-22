import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums + []
        self.arr = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.arr = self.original + []
        return self.arr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.arr)):
            rand_index = random.randint(0, len(self.arr) - 1)
            self.arr[i], self.arr[rand_index] = self.arr[rand_index], self.arr[i]
        
        return self.arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()