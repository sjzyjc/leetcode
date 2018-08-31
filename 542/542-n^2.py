from collections import deque
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0] or len(matrix) == 0 or len(matrix[0]) == 0:
            return [[]]

        height, width = len(matrix), len(matrix[0])
        queue = deque()

        for i in height:
            for j in width:
                if matrix[i][j] != 0:
                    matrix[i][j] = (1 << 31) - 1
                else:
                    queue.append([i, j, 0])
        
        while queue:
            i, j, distance = queue.popleft()

            if not (0<= i < len(matrix) and 0<= j < len(matrix[0])):
                continue     

            if matrix[i][j] < (1 << 31) - 1:
                continue

            matrix[i][j] = distance   

            queue.append([i+1, j, distance + 1])
            queue.append([i-1, j, distance + 1])
            queue.append([i, j+1, distance + 1])
            queue.append([i, j-1, distance + 1])

        return matrix

    def distanceToZero(self, matrix, i, j):
        queue = deque()
        queue.append([i, j, 0])

        while queue:
            i, j, distance = queue.popleft()

            if not (0<= i < len(matrix) and 0<= j < len(matrix[0])):
                continue

            if matirx[i][j] == 0:
                return distance

            queue.append([i+1, j, distance + 1])
            queue.append([i-1, j, distance + 1])
            queue.append([i, j+1, distance + 1])
            queue.append([i, j-1, distance + 1])



                   