from itertools import permutations
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        possibilities = []
        b = []
        m = len(grid[0]) - 1
        n = len(grid) - 1
        
        for i in range(m):
            b.append("d")

        for i in range(n):
            b.append("r")
        

        routes = list(set(list(permutations(b, len(b)))))
        for route in routes:
            possibilities.append(self.move(route,grid))
            
        return min(possibilities)
            
            
            
    def move(self, path: tuple, grid: List[List[int]]) -> int:
        x,y = 0,0
        added = grid[0][0]
        for i in path:
            if i == "r":
                x += 1
            elif i == "d":
                y += 1
            added += grid[x][y]
        
        return added
                
            
            
        