class Solution:
    def splitArray(self, nums: 'List[int]') -> 'bool':
        if not nums or len(nums) < 7:
            return False

        n = len(nums)
        ps = [0] * n
        idxs = collections.defaultdict(list)

        for i in range(n):
            if i == 0:
                ps[i] = nums[i]
            else:
                ps[i] = ps[i - 1] + nums[i]
            idxs[ps[i]].append(i)
        
        for i in range(1, n - 5):
            for k in idxs[ps[n - 1] - ps[i - 1]]:
                if k >= n - 1: break
                if k <= i + 3: continue
                
                for j in idxs[ps[k - 1] - ps[i - 1]]:
                    if j >= k - 1: break
                    if j <= i + 1: continue

                    if j - 1 in idxs[ps[i] + ps[i - 1]]:
                        return True

        return False