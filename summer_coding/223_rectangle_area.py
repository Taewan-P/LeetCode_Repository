class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        r1 = [A,B,C,D]
        r2 = [E,F,G,H]
        
        ra1 = (C-A)*(D-B)
        ra2 = (G-E)*(H-F)
        ra3 = 0
        dx = min(r1[2], r2[2]) - max(r1[0], r2[0]) 
        dy = min(r1[3], r2[3]) - max(r1[1], r2[1]) 
        
        if (dx>=0) and (dy>=0):
            ra3 = dx*dy
            
        return ra1+ra2-ra3