from collections import defaultdict
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        ps = [0 for _ in range(len(nums) + 1)]
        for index, num in enumerate(nums):
            ps[index + 1] = ps[index] + num
            
        l_idx = defaultdict(int)
        largest_l = 0
        for i in range(k, len(nums) - 2 * k + 1):
            if ps[i] - ps[i - k] > largest_l:
                largest_l = ps[i] - ps[i - k]
                l_idx[i] = i - k
            else:
                l_idx[i] = l_idx[i - 1]    
        
        r_idx = defaultdict(int)
        largest_r = 0
        for i in range(len(nums) - 2 * k, k - 1, -1):
            print(i)
            if ps[i + 2 * k] - ps[i + k] >= largest_r:
                largest_r = ps[i + 2 * k] - ps[i + k]
                r_idx[i] = i + k
            else:
                r_idx[i] = r_idx[i + 1]
        
        #print(r_idx, l_idx)
        ans = None
        cur_max = 0
        for i in range(k, len(nums) - 2 * k + 1):
            l = l_idx[i]
            r = r_idx[i]
            
            window = ps[l + k] - ps[l] + ps[r + k] - ps[r] + ps[i + k] - ps[i] 
            if window > cur_max:
                cur_max = window
                ans = [l, i, r]
                
        return ans