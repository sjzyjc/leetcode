class Solution(object):
    def dailyTemperatures(self, tmps):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if not tmps:
            return []
        
        stack = []
        ans = [0 for i in range(len(tmps))]
        for index, tmp in enumerate(tmps):
            while stack and tmp > stack[-1][0]:
                t, i = stack.pop()
                ans[i] = index - i
            
            stack.append([tmp, index])
        
        return ans
                