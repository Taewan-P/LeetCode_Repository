class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [i for i in range(start, start + 2*n, 2)]
        result = arr[0]
        for i in arr[1:]:
            result ^= i
            
        return result