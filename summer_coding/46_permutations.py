from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p = permutations(nums, len(nums))
        return [list(t) for t in list(p)]