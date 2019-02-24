class Solution:
    def findNumberOfLIS(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        
        f = [(1, 1) for _ in range(len(nums))]
        
        max_count = 1
        max_len = 1
        for i in range(1, len(nums)):
            sub_len_max = 0
            sub_len_count = 1
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                    
                if f[j][0] == sub_len_max:
                    sub_len_count += f[j][1]
                
                elif f[j][0] > sub_len_max:
                    sub_len_max = f[j][0]
                    sub_len_count = f[j][1]
                    
            cur_len_max = sub_len_max + 1
            f[i] = (cur_len_max, sub_len_count)
            
            if cur_len_max == max_len:
                max_count += sub_len_count
                
            if cur_len_max > max_len:
                max_len = cur_len_max
                max_count = sub_len_count
                
        #print(f)
        return max_count
                