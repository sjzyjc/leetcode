class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            return False
        
        reverted_num = 0
        for x < reverted_num:
            reverted_num = reverted_num * 10 + x % 10
            x //= 10

        return x == reverted_num or reverted // 10 == x     