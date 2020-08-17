class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # Greedy
        r = 0
        l = 0
        result = 0
        for i in s:
            if i == "R":
                r += 1
            else: # i == "L"
                l += 1
                
            if r == l:
                result += 1
                r = 0
                l = 0
                
        return result