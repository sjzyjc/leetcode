class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if S is None and T is None:
            return True
        
        if (S is None) != (T is None):
            return False
        
        ptr1 = len(S) - 1
        ptr2 = len(T) - 1
        count1 = count2 = 0
        
        while ptr1 >= 0 and ptr2 >= 0:
            while ptr1 >= 0 and S[ptr1] == '#' or count1 > 0:
                if S[ptr1] == '#':
                    count1 += 1
                else:
                    count1 -= 1
                
                ptr1 -= 1
                    
            while ptr2 >=0 and T[ptr2] == '#' or count2 > 0:
                if T[ptr2] == '#':
                    count2 += 1
                else:
                    count2 -= 1
                    
                ptr2 -= 1
            
            if ptr1 >= 0 and ptr2 >= 0:
                #print("compare", S[ptr1], T[ptr2])
                if S[ptr1] != T[ptr2]:
                    return False
                else:
                    ptr1 -= 1
                    ptr2 -= 1
        
        while ptr1 >= 0:
            if S[ptr1] != '#':
                return False
            
            ptr1 -= 2
        
        while ptr2 >= 0:
            if T[ptr2] != '#':
                return False
            
            ptr2 -= 2
            
        return True
            
                
        