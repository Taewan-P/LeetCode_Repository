class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [len(list(filter(lambda x:x < n, nums))) for n in nums]