class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2

            print(mid)
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                print('a')
                return mid
            elif nums[mid] < nums[mid - 1]:
                print('b')
                end = mid - 1
            else:
                print('c')
                start = mid + 1

        return start               

sl = Solution()
print(sl.findPeakElement([1,2,3,1]))