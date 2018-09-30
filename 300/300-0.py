class Solution:
    def lis(self, nums):
        max_sub = 0
        self.hashmap = {}
        for i in range(len(nums)):
            max_sub = max(max_sub, self.dp(nums, i))

        return max_sub

    def dp(self, nums, idx):
        if idx in self.hashmap:
            return self.hashmap[idx]

        max_sub = 1
        for i in range(idx+1, len(nums)):
            if nums[idx] <= nums[i]:
                max_sub = max(max_sub, self.dp(nums, i)+1)

        self.hashmap[idx] = max_sub      
        return max_sub

sl = Solution()
print(sl.lis([19,1,8,3,16,5,20]))