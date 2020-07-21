class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hdegree = 0
        mdegree = 0
        
        if hour != 12:
            hdegree = 30*hour
            
        if minutes != 0:
            mdegree = 6*minutes
            hdegree += 0.5*minutes
            
        ans = abs(hdegree-mdegree)
        
        if ans > 180:
            ans = 360 - ans
        
        return ans