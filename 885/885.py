DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        if not R or not C:
            return []
        
        ans = []
        def checkAndAppend(cur_r, cur_c):
            if 0 <= cur_r < R and 0 <= cur_c < C:
                ans.append([cur_r, cur_c])
        
        checkAndAppend(r0, c0)
        checkAndAppend(r0, c0 + 1)
        checkAndAppend(r0 + 1, c0 + 1)
        checkAndAppend(r0 + 1, c0)
            
        cur_r = r0 + 1
        cur_c = c0 - 1
        checkAndAppend(cur_r, cur_c)
        
        step = 3
        cur_step = 1
        dir_index = 0
        while len(ans) < R * C:
            for _ in range(4):
                while cur_step < step:
                    cur_r += DIRS[dir_index][0]
                    cur_c += DIRS[dir_index][1]
                    
                    checkAndAppend(cur_r, cur_c)
                    cur_step += 1
            
                dir_index = (dir_index + 1) % 4
                cur_step = 0
            
            #start new cycle
            cur_c -= 1
            checkAndAppend(cur_r, cur_c)
            cur_step = 1
            step += 2
            
        return ans
    
            
                
                
            
            
            
        