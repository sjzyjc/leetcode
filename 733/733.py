OFFSETS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image or not image[0]:
            return image
        
        if image[sr][sc] == newColor:
            return image
        
        self.dfs(image, sr, sc, newColor, image[sr][sc])
        return image
    
    def dfs(self, image, row, col, newColor, oldColor):
        if not (0 <= row < len(image) and 0 <= col < len(image[0])):
            return
        
        if image[row][col] != oldColor:
            return
        
        image[row][col] = newColor
        for offset in OFFSETS:
            self.dfs(image, row + offset[0], col + offset[1], newColor, oldColor)
            
        
        