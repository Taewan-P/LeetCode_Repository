class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j] and i < j:
                    ans += 1
            
        return ans