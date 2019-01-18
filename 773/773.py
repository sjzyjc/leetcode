from collections import deque
class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        if not board:
            return 0
        
        visited  = set()
        queue = deque([board])
        ans = 0
        while queue:
            #print(queue)
            length = len(queue)
            for _ in range(length):
                pos = queue.popleft()
                pos_id, i, j = self.getId(pos)
                
                if pos_id == "123450":
                    return ans
                
                visited.add(pos_id)
                for nei in self.findNei(pos, i, j, visited):
                    queue.append(nei)
                    
            ans += 1
            
        return -1
    
    def getId(self, pos):
        pos_id = ""
        zero_i = zero_j = -1
        for i in range(len(pos)):
            for j in range(len(pos[i])):
                pos_id += str(pos[i][j])
                
                if pos[i][j] == 0:
                    zero_i = i
                    zero_j = j
                
        return pos_id, zero_i, zero_j
    
    def findNei(self, pos, zero_i, zero_j, visited):
        ans = []
        offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for offset in offsets:
            nei_i = zero_i + offset[0]
            nei_j = zero_j + offset[1]
            
            if not (0<= nei_i < 2 and 0 <= nei_j < 3):
                continue
                
            new_pos = []
            for row in pos:
                new_pos.append(row + [])
            #print("init", new_pos)
            new_pos[zero_i][zero_j], new_pos[nei_i][nei_j] = new_pos[nei_i][nei_j], new_pos[zero_i][zero_j]

            
            if self.getId(new_pos)[0] in visited:
                continue
                
            #print(new_pos, pos)
            ans.append(new_pos)
        
        return ans
            
        
        