DIR = [[-1, 1], [1, -1]]
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        ans = []
        i = j = 0
        dir_index = 0
        
        ans.append(matrix[i][j])
        while not (i == len(matrix) - 1 and j == len(matrix[0]) - 1):
            while 0 <= i + DIR[dir_index][0] < len(matrix) and 0 <= j + DIR[dir_index][1] < len(matrix[0]):
                i += DIR[dir_index][0]
                j += DIR[dir_index][1]
                ans.append(matrix[i][j])
                
            if dir_index == 0:
                if j + 1 < len(matrix[0]):
                    j += 1
                else:
                    i += 1
            else:
                if i + 1 < len(matrix):
                    i += 1
                else:
                    j += 1
                    
            #print(ans)
            ans.append(matrix[i][j])
            dir_index = 1 - dir_index
            
            
        return ans
                
            
        
            
            
        