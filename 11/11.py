class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_area = -1
        while left < right:
            max_area = max(max_area, (right - left) * min(height[right], height[left]))
            if height[left] == height[right]:
                left += 1
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area