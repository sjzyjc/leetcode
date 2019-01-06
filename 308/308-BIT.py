class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        
        self.matrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        self.bit = [[0 for j in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.update(i, j, matrix[i][j])
        
        #print(self.bit)

    def update(self, i, j, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.matrix[i][j]
        self.matrix[i][j] = val
        bit_i = i + 1
        
        while bit_i < len(self.bit):
            bit_j = j + 1
            while bit_j < len(self.bit[0]):
                self.bit[bit_i][bit_j] += delta
                bit_j += self.lowbit(bit_j)
            
            bit_i += self.lowbit(bit_i)
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        print(self.prefixSum(row2, col2))
        return self.prefixSum(row2, col2) - self.prefixSum(row1 - 1, col2) - self.prefixSum(row2, col1 - 1) + self.prefixSum(row1 - 1, col1 - 1)
   
    def prefixSum(self, i, j):
        ans = 0
        bit_i = i + 1
        bit_j = j + 1
        
        while bit_i > 0:
            bit_j = j + 1
            while bit_j > 0:
                ans += self.bit[bit_i][bit_j]
                bit_j -= self.lowbit(bit_j)
             
            bit_i -= self.lowbit(bit_i)

        return ans
    
    def lowbit(self, x):
        return x & -x
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)