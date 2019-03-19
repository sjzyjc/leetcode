class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pair = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        ans = []
        self.helper(0, n - 1, [None for _ in range(n)], ans, pair)
        return ans
    
    def helper(self, start, end, carry, ans, pair):
        if start > end:
            ans.append("".join(carry))
            return 
        
        for charr in pair:
            if start == end and charr in ['6', '9']:
                continue
                
            if end != 0 and start == 0 and charr == '0':
                continue
                
            carry[start] = charr
            carry[end] = pair[charr]
            self.helper(start + 1, end - 1, carry, ans, pair)
            