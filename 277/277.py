# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return -1
        
        if n == 1:
            return 1
        
        test = 0
        for i in range(1, n):
            if knows(test, i):
                test = i
                
        for i in range(n):
            if not knows(i, test) or (i != test and knows(test, i)):
                return -1
                
        return test