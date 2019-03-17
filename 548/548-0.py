class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 7:
            return False
        
        prefix_sum = [0 for _ in range(len(nums) + 1)]
        for index, num in enumerate(nums):
            prefix_sum[index + 1] = prefix_sum[index] + num
            
        for i in range(1, len(nums) - 5):
            sum_1 = prefix_sum[i] - prefix_sum[0]
            for j in range(i + 2, len(nums) - 3):
                sum_2 = prefix_sum[j] - prefix_sum[i + 1]
                if sum_2 != sum_1:
                    continue
                    
                for k in range(j + 2, len(nums) - 1):
                    sum_3 = prefix_sum[k] - prefix_sum[j + 1]
                    sum_4 = prefix_sum[-1] - prefix_sum[k + 1]
                    if sum_3 != sum_2:
                        continue
                        
                    if sum_1 == sum_2 == sum_3 == sum_4:
                        return True
                    
                    
        return False
            
        