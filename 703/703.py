class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort()
        self.nums = nums
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.insert(val)
        return self.nums[len(self.nums) - self.k]

    def insert(self, val):
        for i in self.nums:
            if self.nums[i] > val:
                break

        self.nums.append(val)
        for j in range(i, len(nums)):
            nums[i] = nums[i - 1]

        nums[i - 1] = val   
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)