class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if S is None:
            S = ""
            
        if T is None:
            T = ""
            
        ptr1 = len(S) - 1
        ptr2 = len(T) - 1
        count_1 = count_2 = 0
        while ptr1 >= 0 or ptr2 >= 0:
            while ptr1 >= 0 and (S[ptr1] == '#' or count_1 > 0):
                if S[ptr1] == '#':
                    count_1 += 1
                else:
                    count_1 -=1
                    
                ptr1 -= 1
                
            while ptr2 >= 0 and (T[ptr2] == '#' or count_2 > 0):
                if T[ptr2] == '#':
                    count_2 += 1
                else:
                    count_2 -= 1
                
                ptr2 -= 1
            
            if ptr1 < 0 and ptr2 >= 0:
                return False
            
            if ptr2 < 0 and ptr1 >= 0:
                return False
            
            if ptr1 >= 0 and ptr2 >= 0 and S[ptr1] != T[ptr2]:
                return False
            
            ptr1 -= 1
            ptr2 -= 1
            
        return True
            