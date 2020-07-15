class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        location = []
        for row in range(len(matrix)):
            location.append([i for i, x in enumerate(matrix[row]) if x == 0])
        
        for i in range(len(location)):
            if location[i]:
                for j in range(len(location[i])):
                    for k in range(len(matrix)):
                        matrix[k][location[i][j]] = 0
                        
                matrix[i] = [0 for _ in matrix[row]]