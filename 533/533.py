from collections import defaultdict
class Solution:
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        if not picture or not picture[0]:
            return 0
        
        hash_count = defaultdict(int)
        col_count = [0 for _ in range(len(picture[0]))]
        
        for i in range(len(picture)):
            tmp = []
            row_count = 0
            for j in range(len(picture[i])):
                if picture[i][j] == 'B':
                    col_count[j] += 1
                    row_count += 1
                    tmp.append(str(j))
                   
            if row_count == N:
                hash_count["-".join(tmp)] += 1
            
        ans = 0
        for key in hash_count:
            if hash_count[key] != N:
                continue
                
            for col in key.split("-"):
                if col_count[int(col)] == N:
                    ans += N
                    
        return ans
                
                
                    
                    
        