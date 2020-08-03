class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for i in set(J):
            result += S.count(i)

        return result