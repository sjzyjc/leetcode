class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        heights = [0 for _ in range(len(matrix[0]))]
        stack = []
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
                    
            stack = []
            for index in range(len(heights) + 1):
                val = heights[index] if index != len(heights) else -1
                while stack and heights[stack[-1]] >= val:
                    h = heights[stack.pop()]
                    right = index
                    left = stack[-1] if stack else -1
                    
                    ans = max(ans, h * (right - left - 1))
                    
                stack.append(index)
                
        return ans
                    
                    
                
                
            
        