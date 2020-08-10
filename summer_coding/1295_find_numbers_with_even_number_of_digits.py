class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            length = len(str(n))
            if length % 2 == 0 and length > 0:
                ans += 1
                
        return ans