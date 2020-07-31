from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        for tup in combinations([_ for _ in range(1,10)], k):
            t = sorted(list(tup))
            if sum(tup) == n:
                if not t in result:
                    result.append(t)
                    
        return result