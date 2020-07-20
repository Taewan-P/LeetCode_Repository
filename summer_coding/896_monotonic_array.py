class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        tmp = sorted(A)
        if tmp == A:
            return True
        else:
            tmp.reverse()
            return True if tmp == A else False