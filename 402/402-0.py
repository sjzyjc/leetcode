class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        T: remove is O(N) which makes it MN
        """
        if not num or len(num) == k:
            return "0"
        
        nums = list(num)
        left, right = 0, 1
        counter = 0
        while right < len(nums) and counter < k:

            if nums[left] > nums[right]:
                nums.remove(nums[left])
                counter += 1
                if left >= 1:
                    left -= 1
                    right -= 1

            else:
                left += 1
                right += 1
                
        if counter < k:
            nums = nums[:len(nums) - (k - counter)]
            
        ret = 0
        for i in nums:
            ret = ret * 10 + int(i)
            
        return str(ret)