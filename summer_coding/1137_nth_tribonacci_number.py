class Solution:
    def tribonacci(self, n: int) -> int:
        return self.bonacci(n,0,1,1)
        
        
    def bonacci(self, n: int, prev1: int, prev2: int, prev3: int) -> int:
        if n == 0:
            return prev1
        elif n == 1:
            return prev2
        elif n == 2:
            return prev3
        else:
            return self.bonacci(n-1, prev2, prev3, prev1 + prev2 + prev3)