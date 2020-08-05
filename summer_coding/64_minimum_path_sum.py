class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        
        if m == 0 or n == 0:
            return 0
        
        for i in range(m):
            if i != 0:
                grid[0][i] += grid[0][i-1]
                
        for j in range(n):
            if j != 0:
                grid[j][0] += grid[j-1][0]
        
        if n == 1:
            return grid[0][-1]
        
        if m == 1:
            return grid[-1][0]
        
        
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[i][j]