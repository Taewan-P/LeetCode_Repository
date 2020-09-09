class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            tmp = []
            for j in range(length-1, -1, -1):
                tmp.append(matrix[j][i])
            
            matrix.append(tmp)

        for i in range(length):
            matrix.pop(0)