import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return math.prod([int(i) for i in list(str(n))]) - sum([int(i) for i in list(str(n))])