class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        
        if len(costs[0]) == 1 and len(costs) == 1:
            return costs[0][0]
        
        min_cost = [[(1 << 31) - 1 for i in range(len(costs[0]))] for j in range(len(costs) + 1)]

                
        for house in range(0, len(costs) + 1):
            for color in range(len(costs[0])):
                if house == 0:
                    min_cost[house][color] = 0
                    continue
                    
                for prev_color in range(len(costs[0])):
                    if prev_color == color:
                        continue
                    
                    min_cost[house][color] = min(min_cost[house][color], min_cost[house - 1][prev_color] + costs[house - 1][color])
                    
        ans = (1 << 31) - 1
        for i in range(len(costs[0])):
            ans = min(ans, min_cost[-1][i])
        
        return ans
                
        