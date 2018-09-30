class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        
        prev_first_min, prev_second_min = (1 << 31) - 1, (1 << 31) - 1
        prev_min_color = -1
        
        for i in range(len(costs[0])):
            cur_val = costs[0][i]
            if cur_val < prev_first_min:
                prev_first_min, prev_second_min = cur_val, prev_first_min
                prev_min_color = i
            elif cur_val < prev_second_min:
                prev_second_min = cur_val
                
        for i in range(1, len(costs)):
            cur_first_min, cur_second_min = (1 << 31) - 1, (1 << 31) - 1
            cur_min_color = -1
            for color in range(len(costs[0])):
                cur_val = costs[i][color]
                if color == prev_min_color:
                    cur_val += prev_second_min
                else:
                    cur_val += prev_first_min
                
                if cur_val < cur_first_min:
                    cur_first_min, cur_second_min = cur_val, cur_first_min
                    cur_min_color = color
                elif cur_val < cur_second_min:
                    cur_second_min = cur_val
                    
            prev_min_color = cur_min_color
            prev_first_min = cur_first_min
            prev_second_min = cur_second_min
            
        return prev_first_min
                
                
        