class UnionFind:
    def __init__(self, board):
        n = len(board) * len(board[0])
        self.parents = [-1 for _ in range(n + 1)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    self.parents[i * len(board[0]) + j] = i * len(board[0]) + j
        
        self.sizes = [1 for _ in range(n + 1)]
        
    def find(self, i, j):
        return self.root(i) == self.root(j)
    
    def union(self, i, j):
        i = self.root(i)
        j = self.root(j)
        
        if self.sizes[i] < self.sizes[j]:
            self.parents[i] = j
            self.sizes[j] += self.sizes[i]
        else:
            self.parents[j] = i
            self.sizes[i] += self.sizes[j]
            
    def root(self, i):
        if self.parents[i] == -1:
            return -1
        
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        
        return i
    
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        height = len(board)
        width = len(board[0])
        offsets = [[1, 0], [0, 1]]
        uf = UnionFind(board)
        for i in range(height):
            for j in range(width):
                if board[i][j] == "X":
                    continue
                
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    uf.union(width * i + j, width * height)
                    
                for offset in offsets:
                    neighbor_i = i + offset[0]
                    neighbor_j = j + offset[1]
                    if not (0 <= neighbor_i < height and 0 <= neighbor_j < width):
                        continue
                    
                    if board[neighbor_i][neighbor_j] == "O":
                        uf.union(width * i + j, width * neighbor_i + neighbor_j)
                        
        for i in range(height):
            for j in range(width):
                if board[i][j] == "X":
                    continue
                    
                if not uf.find(width * i + j, width * height):
                    board[i][j] = "X"
                    
                