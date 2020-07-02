class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 1
        num = 2*n
        
        while(True):
            a = k * (k+1)
            if a < num:
                k += 1
            elif a == num:
                return k
            elif a > num:
                return k-1
                