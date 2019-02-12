class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        stack = []
        ans = 0
        
        for index in range(len(heights) + 1):
            val = heights[index] if index != len(heights) else -1
            while stack and val <= heights[stack[-1]]:
                height = heights[stack.pop()]
                right = index 
                left = stack[-1] if stack else -1
                ans = max(ans, height * (right - left - 1))
                
            stack.append(index)
        
        return ans
                
                
                
        