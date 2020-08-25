class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        mark = []
        nonRotten = 0
        for i, row in enumerate(grid):
            for j, r in enumerate(row):
                if r == 2:
                    # Rotten
                    mark.append((i,j))
                elif r == 1:
                    # Not Rotten
                    nonRotten += 1
        
        row = len(grid)
        col =len(grid[0])
                    
        while mark:
            size = len(mark)
            tmp = []
            for i in range(size):
                x, y = mark.pop(0)
                possibilities = [(x+1, y),(x-1, y),(x, y+1),(x, y-1)]
                for a, b in possibilities:
                    if 0 <= a < row and 0 <= b < col and grid[a][b] == 1:
                        tmp.append((a,b))
                        grid[a][b] = 2
                        nonRotten -= 1
                        
            if tmp:
                mark += tmp
                minutes += 1
            
        return minutes if nonRotten == 0 else -1