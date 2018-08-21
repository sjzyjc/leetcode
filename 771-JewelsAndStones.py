class Solution:
    def numJewelsInStones(self, J, S):
        """
        :time complexity: hashset m+n 
        :no hashset: m*n
        """
        if J is None or S is None:
            return 0

        num = 0
        Jset = set(J)
        for char in S:
            if char in J:
               num += 1

        return num

sl = Solution()
print(sl.numJewelsInStones('aA', 'aAAbbb'))    
print(sl.numJewelsInStones('z', 'ZZZ'))            