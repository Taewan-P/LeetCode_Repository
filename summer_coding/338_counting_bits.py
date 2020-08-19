class Solution:
    def countBits(self, num: int) -> List[int]:
        return ["{0:b}".format(i).count("1") for i in range(num+1)]
