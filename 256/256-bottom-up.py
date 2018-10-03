class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        
        min_cost = [[(1 << 31) - 1 for i in range(3)] for j in range(len(costs) + 1)]
        min_cost[0][0] = 0
        min_cost[0][1] = 0
        min_cost[0][1] = 0
        
        for i in range(1, len(costs) + 1):
            min_cost[i][0] = min(min_cost[i - 1][1], min_cost[i - 1][2]) + costs[i - 1][0]
            min_cost[i][1] = min(min_cost[i - 1][0], min_cost[i - 1][2]) + costs[i - 1][1]
            min_cost[i][2] = min(min_cost[i - 1][0], min_cost[i - 1][1]) + costs[i - 1][2]
            
        
        return min(min_cost[-1][0], min_cost[-1][1], min_cost[-1][2])
