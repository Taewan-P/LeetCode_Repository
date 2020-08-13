class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        else:
            row = ""
            for i,l in enumerate(matrix):
                if not l:
                    return False
                if l[-1] >= target: 
                    row = i
                    break
        
        if row == "":
            return False
        else:
            return True if target in matrix[row] else False