class Solution(object):
    def dailyTemperatures(self, tmps):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if not tmps:
            return []
        
        stack = []
        ret = [0 for i in range(len(tmps))]
        for index, tmp in enumerate(tmps[::-1]):
            if len(stack) == 0:
                stack.append(len(tmps) - index - 1)
                ret[len(tmps) - index - 1] = 0
            else:
                distance = 0
                #print(stack)
                while stack and tmp >= tmps[stack[-1]]:
                    distance += ret[stack.pop()]
                
                if stack:
                    distance += 1
                else:
                    distance = 0
                
                stack.append(len(tmps) - index - 1)
                ret[len(tmps) - index - 1] = distance
                
        return ret
        
               