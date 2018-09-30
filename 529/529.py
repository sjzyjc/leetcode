from collections import deque
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return None
        
        if not click:
            return board
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        queue = deque([(click[0], click[1])])
        child_queue = deque()

        
        while queue:
            x, y = queue.popleft()
            if not (0 <= x < len(board) and 0 <= y < len(board[x])) or not (board[x][y] == 'M' or board[x][y] == 'E'):
                continue
                
            offsets = [[1, 0], [1, -1], [1, 1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1]]
            for offset in offsets:
                child_queue.append((x + offset[0], y + offset[1]))
            
            count = 0
            while child_queue:
                x1, y1 = child_queue.popleft()
                if not (0 <= x1 < len(board) and 0 <= y1 < len(board[x])):
                    continue
            
                if board[x1][y1] == 'M':
                    count += 1
                          
            if count == 0:
                board[x][y] = 'B'
                for offset in offsets:
                    queue.append((x + offset[0], y + offset[1]))
            else:
                board[x][y] = str(count)
        
        return board
                
                