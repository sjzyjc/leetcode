class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.bit = [[0 for j in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.update(i, j, matrix[i][j])
        

    def update(self, row, col, val):
        delta = val - self.matrix[row][col]
        idx_i = row + 1
        
        while idx_i < len(self.bit):
            print(idx_i)
            idx_j = col + 1
            while idx_j < len(self.bit[0]):
                print(idx_j)
                self.bit[idx_i][idx_j] += delta
                idx_j += self.lowbit(idx_j)
                
            idx_i += self.lowbit(idx_i)
        
    
    def lowbit(self, x):

        return x & -x
        

    def sumRegion(self, row1, col1, row2, col2):
        return self.ps(row2, col2) - self.ps(row2, col1 - 1) - self.ps(row1 - 1, col2) + self.ps(row1 - 1, col1 - 1)
    
    def ps(self, row, col):
        ans = 0
        idx_i = row + 1
        while idx_i > 0:
            print(idx_i)
            idx_j = col + 1
            while idx_j > 0:
                ans += self.bit[idx_i][idx_j]
                idx_j -= self.lowbit(idx_j)
                
            idx_i -= self.lowbit(idx_i)
            
        return ans
        
        
matrix = [[1, 2], [3, 4]]
obj = NumMatrix(matrix)
obj.update(0,0,3)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)