class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        orig_index = [i for i in range(len(nums))]
        ans = [0 for _ in range(len(nums))]
        self.mergeSort(nums, 0, len(nums) - 1, orig_index, ans)
        return ans
    
    def mergeSort(self, nums, start, end, orig_index, ans):
        if start >= end:
            return
        
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid, orig_index, ans)
        self.mergeSort(nums, mid + 1, end, orig_index, ans)
        self.merge(nums, start, end, orig_index, ans)
        #print(nums, ans)
        
    def merge(self, nums, start, end, orig_index, ans):
        tmp = []
        mid = (start + end) // 2
        first, second = start, mid + 1
        right_move = 0
        
        while first <= mid and second <= end:
            if nums[first] < nums[second]:
                old_index = orig_index[first]
                tmp.append((nums[first], old_index))
                first += 1
                ans[old_index] += right_move
            elif nums[second] < nums[first]:
                tmp.append((nums[second], orig_index[second]))
                second += 1
                right_move += 1
                
            else:
                tmp.append((nums[first], orig_index[first]))
                tmp.append((nums[second], orig_index[second]))
                first += 1
                second += 1
                ans[orig_index[first]] += right_move
                right_move += 1
                
        while first <= mid:
            tmp.append((nums[first], orig_index[first]))
            ans[orig_index[first]] += right_move
            first += 1
            
        while second <= end:
            tmp.append((nums[second], orig_index[second]))
            second += 1
            
        for i in range(start, end + 1):
            nums[i] = tmp[i - start][0]
            orig_index[i] = tmp[i - start][1]
            
            
        
        