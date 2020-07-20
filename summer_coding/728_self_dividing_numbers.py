class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [n for n in range(left, right+1) if not (False in [True if (i != "0" and n % int(i) == 0) else False for i in list(str(n))])]