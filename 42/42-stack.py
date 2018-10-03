class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        water = 0
        
        for i, val in enumerate(height):
            while stack and val > height[stack[-1]]:
                top = stack.pop()
                
                if len(stack) == 0:
                    break
                width = i - stack[-1] - 1
                bounded_height = min(val, height[stack[-1]]) - height[top]
                water += width * bounded_height
            
            stack.append(i)
        return water
        
            