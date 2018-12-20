class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        
        k = len(costs[0])
        n = len(costs)
        
        pre_first_min, pre_second_min = 0, 0
        pre_min_color = -1
        
        for i in range(n):
            #house i will be painted to k
            first_min = second_min = (1 << 31) - 1
            min_color = -1
            for j in range(k):
                cost = 0
                if j == pre_min_color:
                    cost = pre_second_min + costs[i][j]
                else:
                    cost = pre_first_min + costs[i][j]
                
                if cost <= first_min:
                    second_min = first_min
                    first_min = cost
                    min_color = j
                elif cost < second_min:
                    second_min = cost
                                        
            pre_first_min = first_min
            pre_second_min = second_min
            pre_min_color = min_color
        
        return first_min
                
                
                
                