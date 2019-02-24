class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        
        self.helper(matrix, 0, len(matrix))
        
    def helper(self, m, s, l):
        if l <= 1:
            return
        
        for i in range(l - 1):
            m[s][s + i], m[s + i][s + l - 1], m[s + l - 1][s + l - 1 - i], m[s + l - 1 - i][s] = m[s + l - 1 - i][s], m[s][s + i], m[s + i][s + l - 1], m[s + l - 1][s + l - 1 - i]
            
        self.helper(m, s+1, l - 2)
        