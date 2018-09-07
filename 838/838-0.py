class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        if not dominoes and len(dominoes) == 1:
            return dominoes
        
        listt = list(dominoes)
        listt.insert(0, 'L')
        listt.append('R') 
        
        i, j = 0, 1
        while j < len(listt) - 1:
            while listt[j] == '.':
                j += 1
            
            if listt[j] == 'L':
                if listt[i] == 'L':
                    while i < j:
                        listt[i] = 'L'
                        i += 1
                else:
                    length = j - i - 1
                    
                    while i <= j - length // 2 - 1:
                        listt[i] = 'R'
                        i += 1
                    while i < j:
                        listt[i] = 'L'
                        i += 1
                    if length % 2 == 1:
                        listt[j - length // 2 - 1] = '.'
            else: 
                if listt[i] == 'L':
                    i = j
                else:
                    while i < j:
                        listt[i] = 'R'
                        i += 1
            
            j += 1
                            
        
        return "".join(listt[1: len(listt) - 1])
        
        
        