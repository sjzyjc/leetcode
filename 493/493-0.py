class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.ans = 0
        self.mergeSort(0, len(nums) - 1, nums)
        
        return self.ans
        
    def mergeSort(self, start, end, nums):
        if start >= end:
            return
        
        mid = (start + end) // 2
        self.mergeSort(start, mid, nums)
        self.mergeSort(mid + 1, end, nums)
        
        self.merge(nums, start, end)
        
    def merge(self, A, start, end):
        tmp = []
        mid = (end + start) // 2
        left_count = 0
        
        first_half_index, second_half_index = start, mid + 1
        while first_half_index <= mid:
            while second_half_index <= end and A[first_half_index] > A[second_half_index] * 2:
                second_half_index += 1
            
            self.ans += (second_half_index - mid - 1)
            first_half_index += 1
        #print(self.ans)
        
        first_half_index, second_half_index = start, mid + 1
        while first_half_index <= mid and second_half_index <= end:
            if A[first_half_index] <= A[second_half_index]:
                tmp.append(A[first_half_index])
                first_half_index += 1
            else:
                tmp.append(A[second_half_index])
                second_half_index += 1

        if first_half_index <= mid:
            tmp.extend(A[first_half_index: mid + 1])      

        if second_half_index <= end:
            tmp.extend(A[second_half_index: end + 1])
            
        #print("merge", tmp, start, end)
        for index, value in enumerate(tmp):
            #print(start+index)
            A[start + index] = value          
        
        
