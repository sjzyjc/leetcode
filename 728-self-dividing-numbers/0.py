class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSelfDividingNum(number):
            for char in str(number):
                if int(char) == 0 or number % int(char) != 0:
                    return False
            return True         

        if left < 1:
            left = 1

        if right > 10000:
            right = 10000

        result = []
        for i in range(left, right+1):
            if isSelfDividingNum(i):
                result.append(i)

        return result        

sl = Solution()
print(sl.selfDividingNumbers(1,22))      
print(sl.selfDividingNumbers(-10,22))                  