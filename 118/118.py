class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        ans = []
        ans.append([1])
        ans.append([1, 1])
        
        prev = [1, 1]
        for i in range(3, numRows + 1):
            row = [1]
            for j in range(1, i - 1):
                #print(prev, j-1, j)
                row.append(prev[j - 1] + prev[j])
                
            row.append(1)
            ans.append(row)
            prev = row
            
        return ans
                