class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        freq = [0 for i in range(0, 20001)]
        for num in nums:
            freq[num + 10000] += 1

        ans = 0
        carry = 0
        
        for i in range(len(freq)):
            if freq[i] != 0:
                ans += (i - 10000) * ((freq[i] - carry) // 2)
                if (freq[i] - carry) % 2 == 1:
                    carry = 1
                    ans += (i - 10000)
                else:
                    carry = 0
        return ans
                
                    
        