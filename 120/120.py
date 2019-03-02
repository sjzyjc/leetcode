class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        
        f = [(1 << 31) - 1 for _ in range(len(triangle[-1]))]
        for i in range(len(triangle[0])):
            f[i] = triangle[0][i]
            
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i]) - 1, -1, -1):
                #print(i,j, f[j - 1], f[j], triangle[i][j])
                if j > 0:
                    f[j] = min(f[j - 1], f[j]) + triangle[i][j]
                else:
                    f[j] += triangle[i][j]
                    
        return min(f)
                
        