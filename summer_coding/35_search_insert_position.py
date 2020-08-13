class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i,j in enumerate(nums):
                if j > target:
                    return i
                
            return i+1