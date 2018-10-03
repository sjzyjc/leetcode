class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        min_cost = (1 << 31) - 1
        self.hashMap = {}
        return self.dp(costs, -1, -1)


    def dp(self, costs, i, j):
        if i > len(costs) - 1:
            return 0

        if (i, j) in self.hashMap:
            return self.hashMap[(i, j)]

        min_sub = (1 << 31) - 1
        cur_value = costs[i][j]
        if i == -1 and j == -1:
            cur_value = 0
        for color in range(3):
            if color != j:
                min_sub = min(min_sub, self.dp(costs, i + 1, color) + cur_value)

        self.hashMap[(i,j)] = min_sub 
        return min_sub
        