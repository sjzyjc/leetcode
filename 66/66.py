class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        length = len(digits)
        bit_counter = 1
        ans = 0
        for digit in digits:
            ans += digit * (10 ** (length - bit_counter))
            bit_counter += 1
            
        ans = str(ans + 1)
        ans_list = []
        for charr in ans:
            ans_list.append(int(charr))
        
        return ans_list
        